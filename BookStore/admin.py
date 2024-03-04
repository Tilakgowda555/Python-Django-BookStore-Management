from django.contrib import admin

from BookStore.models import Category, City, Author, Book

# Register your models here.

admin.site.register(Category)
admin.site.register(City)
admin.site.register(Author)
admin.site.register(Book)

