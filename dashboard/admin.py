from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
	pass
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
	pass
admin.site.register(Category, CategoryAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
	pass
admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductClassAdmin(admin.ModelAdmin):
	pass
admin.site.register(ProductClass, ProductClassAdmin)

class ProductAttributeAdmin(admin.ModelAdmin):
	pass
admin.site.register(ProductAttribute, ProductAttributeAdmin)

class ProductAttributeValueAdmin(admin.ModelAdmin):
	pass
admin.site.register(ProductAttributeValue, ProductAttributeValueAdmin)
