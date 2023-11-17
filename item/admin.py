"""
Registers the Category and Item models with the Django admin site.

This allows the Category and Item models to be managed through the admin interface.
"""

from django.contrib import admin

from .models import Category, Item

# admin.py

admin.site.register(Category)
admin.site.register(Item)