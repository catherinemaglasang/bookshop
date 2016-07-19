from django.conf.urls import include, url
from django.contrib import admin
from shop import views

urlpatterns = [
    
    url(r'^$', 'dashboard.views.home', name='home'),
    
    url(r'^view_all/$', 'dashboard.views.view_all', name='view_all'),

    url(r'^products/$', 'dashboard.views.product_list', name='product_list'),
    url(r'^products/(?P<product_id>[0-9]+)/$', 'dashboard.views.view_product', name='view_product'),
    url(r'^add_product/$', 'dashboard.views.add_product', name='add_product'),
    url(r'^delete_product/(?P<product_id>[0-9]+)/$', 'dashboard.views.delete_product', name='delete_product'),
    url(r'^update_product/(?P<product_id>[0-9]+)/$', 'dashboard.views.update_product', name='update_product'),
   
    url(r'^category_list/$', 'dashboard.views.category_list', name='category_list'),
    url(r'^add_category/$', 'dashboard.views.add_category', name='add_category'),
    url(r'^delete_category/(?P<category_id>[0-9]+)/$', 'dashboard.views.delete_category', name='delete_category'),
    url(r'^update_category/(?P<category_id>[0-9]+)/$', 'dashboard.views.update_category', name='update_category'),

    url(r'^productCategories/$', 'dashboard.views.productCategories', name='productCategories'),
    url(r'^add_productCategory/$', 'dashboard.views.add_productCategory', name='add_productCategory'),
    
    url(r'^productClasses/$', 'dashboard.views.productClass_list', name='productClass_list'),
    url(r'^add_productClass/$', 'dashboard.views.add_productClass', name='add_productClass'),
    
    url(r'^productAttributes/$', 'dashboard.views.productAttribute_list', name='productAttribute_list'),
    url(r'^add_productAttribute/$', 'dashboard.views.add_productAttribute', name='add_productAttribute'),
    
    url(r'^productAttributeValues/$', 'dashboard.views.productAttributeValue_list', name='productAttributeValue_list'),
    url(r'^add_productAttributeValue/$', 'dashboard.views.add_productAttributeValue', name='add_productAttributeValue'),

]
