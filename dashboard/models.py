from django.db import models

class Product(models.Model):
	"""docstring for product"""
	title = models.CharField(max_length=100, null=True)
	description = models.CharField(max_length=200, null=True)
	
	def __unicode__(self):
		return " ".join((unicode(self.title),unicode(self.description)))


class Category(models.Model):
	name = models.CharField(max_length = 50, null = True)
	description =  models.TextField()

	def __unicode__(self):
		return self.name

class ProductCategory(models.Model):
	product = models.ForeignKey('Product')
	category = models.ForeignKey('Category')

class ProductClass(models.Model):
	name = models.CharField(max_length=50, null=True)

	def __unicode__(self):
		return self.name

class ProductAttribute(models.Model):
	name = models.CharField(max_length=50, null=True)
	code = models.CharField(max_length=50, null=True)
	productClass = models.ForeignKey('ProductClass')

	def __unicode__(self):
		return " ".join((unicode(self.name),unicode(self.code)))

class ProductAttributeValue(models.Model):
	product = models.ForeignKey('Product')
	value = models.CharField(max_length=50, null=True)
	attribute = models.ForeignKey('ProductAttribute')

