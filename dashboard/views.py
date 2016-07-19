from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import *
from .forms import *
from django.contrib import messages


def home(request):
	return render(request, 'dashboard/home.html', {})

def product_list(request):
	products = Product.objects.all()
	productLen = products.count()
	return render(request, 'dashboard/products/products.html', {
		'products': products,
		'productLen': productLen,
	})


def add_product(request):
	form = ProductForm(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if  form.is_valid():
			form.save()
			return HttpResponseRedirect('/dashboard/add_productCategory/')

	return render(request, 'dashboard/products/add_product.html', {
	 'form': form
	  })

def delete_product(request, product_id):
	products = Product.objects.all()
	p = Product.objects.get(pk=product_id)
	p.delete()

	return HttpResponseRedirect('/dashboard/products/')

def update_product(request, product_id):
	product = Product.objects.get(pk=product_id)
	update_product_form = ProductForm(request.POST or None, instance=product)

	if request.method == 'POST':
		if update_product_form.is_valid():
			update_product_form.save()
			
        	return HttpResponseRedirect('/dashboard/products/')

	return render(request, 'dashboard/products/update_product.html', {'form':update_product_form,})
	
def view_product(request, product_id):
	product = Product.objects.get(id=product_id)
	return render(request, 'dashboard/products/products.html', {'product': product})



def category_list(request):
	categories = Category.objects.all()
	categoryLen = categories.count()
	return render(request, 'dashboard/products/categories.html', {
		'categories': categories,
		'categoryLen': categoryLen,
	})

def add_category(request):
	form = CategoryForm(request.POST or None)
	if request.method == 'POST':
		if  form.is_valid():
			form.save()
			
			return HttpResponseRedirect('/dashboard/add_productCategory/')

	return render(request, 'dashboard/products/add_category.html', {'form': form})

def delete_category(request, category_id):
	categories = Category.objects.all()
	c = Category.objects.get(pk=category_id)
	c.is_active = False
	c.delete()

	return HttpResponseRedirect('/dashboard/category_list/')

def update_category(request, category_id):
	category = Category.objects.get(pk=category_id)
	update_category_form = CategoryForm(request.POST or None, instance=category)

	if request.method == 'POST':
		if update_category_form.is_valid():
			update_category_form.save()
			return HttpResponseRedirect('/dashboard/category_list/')

	return render(request, 'dashboard/products/update_category.html', {'form':update_category_form,})
	


def productCategories(request):
	active_productCategories = ProductCategory.objects.all()
	return render(request, 'dashboard/products/productCategories.html', {
		'productCategories': active_productCategories,
	})


def add_productCategory(request):
	form = ProductCategoryForm(request.POST or None)
	if request.method == 'POST':
		if  form.is_valid():
			form.save()
			return HttpResponseRedirect('/dashboard/add_productAttributeValue/')

	return render(request, 'dashboard/products/add_productCategory.html', {
	 'form': form
	  })


def productClass_list(request):
	productClasses = ProductClass.objects.all()
	productClassLen = productClasses.count()
	return render(request, 'dashboard/products/productClasses.html', {
		'productClasses': productClasses,
		'productClassLen': productClassLen,
	})

def add_productClass(request):
	form = ProductClassForm(request.POST )
	if request.method == 'POST':
		if  form.is_valid():
			form.save()
			return HttpResponseRedirect('/dashboard/productClasses/')

	return render(request, 'dashboard/products/add_productClass.html', {
	 'form': form
	  })

def productAttribute_list(request):
	productAttributes = ProductAttribute.objects.all()
	productAttributeLen = productAttributes.count()
	return render(request, 'dashboard/products/productAttributes.html', {
		'productAttributes': productAttributes,
		'productAttributeLen': productAttributeLen,
	})

def add_productAttribute(request):
	form = ProductAttributeForm(request.POST )
	if request.method == 'POST':
		if  form.is_valid():
			form.save()
			return HttpResponseRedirect('/dashboard/productAttributes/')

	return render(request, 'dashboard/products/add_productAttribute.html', {
	 'form': form
	  })

def productAttributeValue_list(request):
	productAttributeValues = ProductAttributeValue.objects.all()
	productAttributeValueLen = productAttributeValues.count()
	return render(request, 'dashboard/products/productAttributeValues.html', {
		'productAttributeValues': productAttributeValues,
		'productAttributeValueLen': productAttributeValueLen,
	})

def add_productAttributeValue(request):
	form = ProductAttributeValueForm(request.POST )
	if request.method == 'POST':
		if  form.is_valid():
			form.save()
			return HttpResponseRedirect('/dashboard/productClasses/')

	return render(request, 'dashboard/products/add_productAttributeValue.html', {
	 'form': form
	  })

def view_all(request):
	return render(request, 'dashboard/products/view_all.html', {})
