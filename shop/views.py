from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import *
from .forms import *

def home(request):
	return render(request, 'shop/blog_post.html', {})

def login_user(request):
	return render(request, 'shop/login.html', {})

def register(request):
	return render(request, 'shop/register.html', {})

def promotions(request):
	""" This serves as the landing page of the store """ 
	products = [{'id': '1', 'title': 'Product 1', 'description' : 'Product 1 Description', 'primary_image': '/static/img/500x500.png', 'link_url': '#/product/1', 'features' : ['Free Shipping'], 'old_price': '1000', 'current_price': '800'}, {'title': 'Product 1', 'description' : 'Product 1 Description', 'primary_image': '/static/img/500x500.png', 'link_url': '#/product/1', 'features' : ['Free Shipping'], 'old_price': '1000', 'current_price': '800'}, {'title': 'Product 1', 'description' : 'Product 1 Description', 'primary_image': '/static/img/500x500.png', 'link_url': '#/product/1', 'features' : ['Free Shipping'], 'old_price': '1000', 'current_price': '800'}]

	categories = [{'title': 'Tech', 'description': 'Tech Description', 'product_count': '152', 'primary_image': '/static/img/100x100.png'}, {'title': 'Home', 'description': 'Home Description', 'product_count': '100', 'primary_image': '/static/img/100x100.png'}];
	category_tree = [{'parent': 'Tech', 'children': [{'parent': 'Laptops', 'children': ['Mac', 'Ultra Books']}]}]

	tags = ['New Season', 'Watches', 'Classic'];
	promotions = [{'title': 'Save up to $150 on Your Next Laptop', 'description': 'I\'m Not Gonna Pay A Lot For This Laptop.', 'btn_link': '/#', 'btn_text': 'Shop Now', 'is_banner': 'true', 'primary_image': '/static/img/test_slider/1-i.png'}, {'title': 'Save up to $150 on Your Next Laptop', 'description': 'I\'m Not Gonna Pay A Lot For This Laptop.', 'btn_link': '/#', 'btn_text': 'Shop Now', 'is_banner': 'true', 'primary_image': '/static/img/test_slider/1-i.png'}];

	store = [{'primary_logo': '/static/img/logo-w.png', 'name': 'TheStore', 'description': 'Store in a box'}];

	brands = [{'title': 'Apple', 'item_count': 50}, {'title': 'Orange', 'item_count': 50}, ]
	
	return render(request, 'shop/home.html', {
		'products': products, 
		'promotions': promotions, 
		})

def catalogue(request):
	""" Page showing all products in store """
	return render(request, 'shop/catalogue.html', {})

def shop_category(request):
	""" Category page of shop """ 
	return render(request, 'shop/category_page.html', {})

def single_product(request):
	""" Single product view """
	return render(request, 'shop/single_product.html', {})
	
def cart(request):
	cart_items = [{'price': '13', 'quantity': '1', 'title': 'Gucci Patent Leather Open Toe Platform', 'item_link': '#/', 'primary_image': '/static/img/100x100.png'}];
	cart = {'total': '150', 'items': cart_items, 'shipping_fee': '0', 'total_tax': '0'};
	return render(request, 'shop/cart.html', {
		'cart_items': cart_items, 
		'cart': cart,
		})

def checkout(request):
	return render(request, 'shop/checkout.html', {})
