from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, UserManager
from django.conf import settings

"""
1. Product
2. Auction
3. Blog
4. Category
5. Cart
6. ProductClass 
7. Category
8. ProductCategory 
9. Product
10. ProductAttribute
11. ProductAttributeValue
12. ProductImage
"""
# Create your models here.
class Product(models.Model):
	"""docstring for product"""
	title = models.CharField(max_length=100, null=True)
	author = models.CharField(max_length=100, null=True)
	description = models.CharField(max_length=200, null=True)
	price = models.DecimalField(default = 0, max_digits = 100, decimal_places = 2)
	avatar = models.ImageField('avatar', upload_to='avatar', default='img/images.jpg')
	
	def __unicode__(self):
		return self.title


class Category(models.Model):
	name = models.CharField(max_length = 50, null = True)
	description =  models.TextField()

	def __unicode__(self):
		return self.name

class ProductCategory(models.Model):
	product = models.ForeignKey('Product')
	category = models.ForeignKey('Category')

class Auction(models.Model):
	auctionItem = models.ForeignKey('Product')
	price = models.DecimalField(default=0, max_digits=100, decimal_places=2)

class BlogCategory(models.Model):
	name = models.CharField(max_length = 50, null = True)
	description =  models.TextField()

	def __unicode__(self):
		return self.name

class Blog(models.Model):
	author = models.ForeignKey(User, null=True )
	title = models.CharField(max_length=200)
	text = models.TextField()
	category = models.ForeignKey('BlogCategory',blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank = True , null = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save

	def __unicode__(self):
		return self.title

# class Order(models.Model):
# 	product = models.ForeignKey(null=True, blank=True, on_delete=models.PROTECT)
# 	order_date = models.DateTimeField(blank = True , null = True)

# 	def __unicode__(self):
# 		return self.product

# class OrderLine(models.Model):

# class OrderConfirmation(models.Model)