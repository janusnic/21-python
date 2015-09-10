from django.contrib import admin

# Register your models here.
from .models import Category, Blog, Author, Entry 

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)