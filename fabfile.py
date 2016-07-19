from __future__ import with_statement
import django
django.setup()
import os
import sys
from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import call_command
from oscar.apps.promotions.models import *

from fab_deploy import *
from fabric.contrib.console import confirm
from fabric.api import env, cd, prefix, local, sudo as _sudo, run as _run, hide, task, settings, abort
from fabric.contrib.files import exists, upload_template
from fabric.colors import yellow, green, blue, red
from fabric.operations import _prefix_commands, _prefix_env_vars
from contextlib import contextmanager

"""
Run:
fab deploy
fab post_deploy

Reload changes to server:
fab post_reload
"""

""" Global Configurations """
ssh_user = 'roselle'
project_dir = '/home/%s/sites' % (ssh_user)
project_name = 'bookshop'
project_root = '%s/%s' % (project_dir, project_name)
venv_path = ''
repo_url = 'https://bitbucket.org/motethansen/bookshop'

""" DB Configurations """
db_name = 'bookshopdb'
db_user = 'bookshop'
db_pass = 'bookshop'

""" Templates """
templates = {
    "nginx": {
        "local_path": "/home/roselle/sites/bookshop/deploy/nginx/bookshop.conf",
        "remote_path": "/etc/nginx/sites-available/bookshop.conf",
        "remote_path2": "/etc/nginx/sites-enabled/bookshop.conf", 
        "reload_command": "service nginx restart",
    },
    "supervisor": {
        "local_path": "/home/roselle/sites/bookshop/deploy/supervisor/bookshop.conf",
        "remote_path": "/etc/supervisor/conf.d/bookshop.conf",
        "reload_command": "supervisorctl reload",
    },
    "gunicorn": {
        "local_path": "/home/roselle/sites/bookshop/deploy/gunicorn/gunicorn_start",
    },
    "solr": {
        "local_conf": "/home/roselle/sites/bookshop/deploy/solr/solr_conf",
        "remote_path": "/home/roselle/sites/bookshop/deploy/solr/solr-4.7.2/example/solr/collection1/conf",
    },
    "uwsgi": {
        "local_conf": "/home/roselle/sites/bookshop/deploy/uwsgi/bookshop.ini", 
        "remote_conf": "/etc/uwsgi/sites/bookshop.ini",
        "local_upstart": "/home/roselle/sites/bookshop/deploy/uwsgi/uwsgi.conf", 
        "remote_upstart": "/etc/init/uwsgi.conf",
    }
}

""" Global Commands """
def prod():
    # care4sos.dk # Moved to same server
    env.hosts = ['roselle@188.166.250.1']
    env.user = 'roselle'
    env.password = 'Dette3rfork3rt'

def staging():
    # shop.care4sos.dk
    env.hosts = ['roselle@128.199.246.173']
    env.user = 'roselle'
    env.password = 'Dette3rFork3rt'

@contextmanager
def virtualenv():
    """
    Runs commands within the project's virtualenv.
    """
    with cd(project_root):
        with prefix("source venv/bin/activate"):
            yield

""" Pre-deployment Commands """
def prepare_db():
    """ Setup Postgresql Database """
    try: 
        run('sudo su - postgres psql -c "dropdb %s"' % (db_name))
        run('sudo su - postgres psql -c "dropuser %s"' % (db_user))
    except: pass
    run('sudo su - postgres psql -c "createdb %s;"' % (db_name))
    run('sudo su - postgres psql -c "createuser -P -s -d -r %s"' % (db_user))

def prepare_git():
    try: 
        local("git add -A && git commit")
        local("git push")
    except: pass

def prepare_packages():
    sudo("apt-get update")
    sudo("apt-get upgrade")
    sudo("apt-get install nginx postgresql memcached supervisor redis-server mercurial python-dev libpq-dev memcached unixodbc-dev git-core")
    sudo("apt-get install python-dev python-setuptools libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk")
    sudo("apt-get install libjpeg62 libjpeg62-dev zlib1g-dev")
    sudo("apt-get install supervisor")
    sudo("apt-get install libjpeg-dev")
    sudo("easy_install pip")
    sudo("pip install virtualenv")

def prepare_server_config():
    sudo("apt-get purge nginx")
    sudo("apt-get purge supervisor")
    sudo("apt-get purge gunicorn")
    sudo("apt-get install nginx supervisor gunicorn")

    """ prepare nginx """ 
    prepare_nginx()
    
    """ prepare uwsgi """
    prepare_uwsgi()
    
    """ prepare supervisor """ 
    # prepare_supervisor()

    """ Reload Server """
    reload_server()

def prepare_nginx():
    if exists(templates['nginx']['remote_path']):
        sudo("rm %s" % templates['nginx']['remote_path'])
        sudo("rm %s" % templates['nginx']['remote_path2'])
        
    # sudo("cp %s %s" % (templates['nginx']['local_path'], templates['nginx']['remote_path']))
    with cd(project_root):
        sudo("cp %s %s" % ('deploy/uwsgi/nginx.conf', '/etc/nginx/sites-available/bookshop.conf'))
    sudo("ln -s %s %s" % (templates['nginx']['remote_path'], templates['nginx']['remote_path2']))
    with cd(project_root):
        if exists("deploy/logs"):
            sudo("rm -r deploy/logs")
        sudo("mkdir deploy/logs")
        sudo("touch deploy/logs/nginx-access.log")
        sudo("touch deploy/logs/nginx-error.log")
        sudo("touch deploy/logs/gunicorn.log")

def prepare_uwsgi():
    """ First remove all traces of pre-installed uwsgi """
    sudo("initctl stop uwsgi")
    if exists('/etc/init/uwsgi.conf'):
        sudo("rm -r /etc/init/uwsgi.conf")

    sudo("pip uninstall uwsgi")
    sudo("pip install uwsgi")

    # Installing via pip, you get the executable at /usr/local/bin/uwsgi
    # Use upstart instead of sysvinit

    """ Setup pip upstart script """
    with cd(project_root):
        sudo("cp %s %s" % ('deploy/uwsgi/uwsgi.conf', '/etc/init/uwsgi.conf'))
        sudo("cp %s %s" % ('deploy/uwsgi/bookshop.ini', '/etc/uwsgi/vassals/bookshop.ini'))
    sudo("initctl start uwsgi")




    # if exists(templates['uwsgi']['remote_upstart']):
        # sudo("rm %s" % templates['uwsgi']['remote_upstart'])
    # sudo("mkdir -p %s" % templates['uwsgi']['remote_conf'])
    # sudo("cp %s %s" % (templates['uwsgi']['local_conf'], templates['uwsgi']['remote_conf']))
    # sudo("cp %s %s" % (templates['uwsgi']['local_upstart'], templates['uwsgi']['remote_upstart'])) 

def prepare_supervisor():
    if exists(templates['supervisor']['remote_path']):
        sudo("rm %s" % templates['supervisor']['remote_path'])
    sudo("cp %s %s" % (templates['supervisor']['local_path'], templates['supervisor']['remote_path']))
   
    with cd(project_root):
        sudo("chmod u+x deploy/gunicorn/gunicorn_start")

def reload_server():
    """ reload configurations """ 
    sudo("service nginx restart")
    sudo("service nginx reload")
    # sudo("service uwsgi start")
    # sudo("service supervisor start")
    # sudo("supervisorctl reread")
    # sudo("supervisorctl update")
    # sudo("supervisorctl start gunicorn")

def deploy():
    """ 
    Utility function for deployment: This fab script deploys your local django app 
    to your remote server using Gunicorn, Supervisor & Nginx. Addons: Solr/Haystack, Celery, 
    Redis/Memcache. 
    
    Make sure that key-based authentication between server and local is enabled (See id_rsa)
    """
    
    """ Stop all current services/processes """
    sudo("supervisorctl stop all")

    """Prepare Local"""
    prepare_git() 

    """Prepare Remote Server"""
    prepare_packages()

    """ Prepare Database """ 
    prepare_db()

    """ Create directory for project """ 
    if exists(project_dir):
        sudo("rm -r %s" % project_dir)
    run("mkdir %s" % (project_dir))

    """ Clone repository """ 
    with cd(project_dir):
        run("git clone %s" % (repo_url))

    """Setup virtualenv and install requirements"""
    with cd(project_root):
        run("virtualenv venv")
        with virtualenv():
            run("pip install -r requirements.txt")
            run("pip install gunicorn")
            run("pip install Pillow --upgrade")
        run("venv/bin/python manage.py migrate")
        run("venv/bin/python manage.py syncdb")

    """ Post Deployment Configurations """
    with virtualenv():
        with cd(project_root):
            run("pip install pycountry")
            run("python manage.py oscar_populate_countries")
            run("python manage.py collectstatic")
            run("python manage.py thumbnail cleanup")


    """ Prepare gunicorn or uwsgi & nginx """ 
    prepare_server_config()

    """ Populate data """ 
    post_deploy()


def post_deploy():
    with virtualenv(): 
        with cd(project_root):
            run("python manage.py populate_data")

def post_reload():
    prepare_git() 
    with virtualenv():
        with cd(project_root):
            sudo("git pull origin master")
    reload_server()
