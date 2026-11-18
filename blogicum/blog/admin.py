from django.contrib import admin
from .models import Post, Category
from .models import Location

models = Post, Category, Location
admin.site.register(models) 