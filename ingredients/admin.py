from django.contrib import admin

from ingredients.models import Category, Ingredient

admin.site.register([Ingredient, Category])