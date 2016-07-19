"""config URL Configuration

The `urlpatterns` list routes URLs to shop.views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', shop.views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from shop import views

urlpatterns = [
    url(r'^$', 'shop.views.promotions', name='promotions'),

    url(r'^login/$', 'shop.views.login_user', name='login'),
    url(r'^register/$', 'shop.views.register', name='register'),

    url(r'^category/$', 'shop.views.shop_category', name='shop_category'),
    url(r'^catalogue/$', 'shop.views.catalogue', name='catalogue'),
    url(r'^product/$', 'shop.views.single_product', name='product'),
    
    url(r'^cart/$', 'shop.views.cart', name='cart'),
    url(r'^checkout/$', 'shop.views.checkout', name='checkout'),
]

