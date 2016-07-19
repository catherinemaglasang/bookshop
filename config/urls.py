from django.conf.urls import include, url
from django.contrib import admin
# from shop import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = {
    url(r'^admin/', include(admin.site.urls)),

    # Shop Views
    url(r'^', include('shop.urls', namespace='shop')),
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),
    url(r'^blog/', include('blog.urls', namespace='blog')),}