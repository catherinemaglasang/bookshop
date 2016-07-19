from django import forms
from django.forms import fields, models
from .models import *


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('title', 'description')

	def __init__(self, *args, **kwargs):
		super(ProductForm,self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs['class'] = 'form-control'
		self.fields['description'].widget.attrs['class'] = 'form-control'

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('name', 'description')

	def __init__(self, *args, **kwargs):
		super(CategoryForm,self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['class'] = 'form-control'
		self.fields['description'].widget.attrs['class'] = 'form-control'
		
class ProductCategoryForm(forms.ModelForm):
	class Meta:
		model = ProductCategory
		fields = ('product', 'category')

	def __init__(self, *args, **kwargs):
		super(ProductCategoryForm,self).__init__(*args, **kwargs)
		self.fields['product'].widget.attrs['class'] = 'form-control'
		self.fields['category'].widget.attrs['class'] = 'form-control'

class ProductClassForm(forms.ModelForm):
	class Meta:
		model = ProductClass
		fields = ('name',)

class ProductAttributeForm(forms.ModelForm):
	class Meta:
		model = ProductAttribute
		fields = ('name', 'code', 'productClass')

class ProductAttributeValueForm(forms.ModelForm):
	class Meta:
		model = ProductAttributeValue
		fields = ('product', 'value', 'attribute')

	# def __init__(self, *args, **kwargs):
	# 	super(AuctionForm,self).__init__(*args, **kwargs)
	# 	self.fields['auctionItem'].widget.attrs['class'] = 'form-control'
	# 	self.fields['price'].widget.attrs['class'] = 'form-control'

