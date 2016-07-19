from django import forms
from django.forms import fields, models
from .models import *


class BlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ('author', 'title', 'text', 'category', 'created_date', 'published_date')

	def __init__(self, *args, **kwargs):
		super(BlogForm,self).__init__(*args, **kwargs)
		self.fields['author'].widget.attrs['class'] = 'form-control'
		self.fields['title'].widget.attrs['class'] = 'form-control'
		self.fields['text'].widget.attrs['class'] = 'form-control'
		self.fields['category'].widget.attrs['class'] = 'form-control'
		self.fields['created_date'].widget.attrs['class'] = 'form-control'
		self.fields['published_date'].widget.attrs['class'] = 'form-control'