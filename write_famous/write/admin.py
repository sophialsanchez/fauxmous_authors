from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
	list_display = ('book_author', 'book_title')
	
# Register your models here.
admin.site.register(Book, BookAdmin)