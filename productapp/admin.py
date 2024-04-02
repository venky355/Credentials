from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity','image')  

admin.site.register(Product, ProductAdmin)

