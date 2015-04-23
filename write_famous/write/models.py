from django.db import models

# Create your models here.

class Book(models.Model):
	book_author = models.CharField(max_length=50)
	book_title = models.CharField(max_length=1000)
	book_text = models.TextField(max_length=10000)
	slug = models.SlugField(max_length=50)
	def __str__(self):
		return self.book_author