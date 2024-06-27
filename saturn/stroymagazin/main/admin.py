from django.contrib import admin
from .models import Product

admin.site.register(Product)


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']
