from django.db import models


class Blog(models.Model):
	author = models.CharField(max_length=50, null=True)
	title = models.CharField(max_length=200)
	text = models.TextField()
	# created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank = True , null = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save

	def __unicode__(self):
		return self.title

class Category(models.Model):
	name = models.CharField(max_length = 50, null = True)
	description =  models.TextField()

	def __unicode__(self):
		return self.name
