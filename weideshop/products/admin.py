from mptt.admin import MPTTModelAdmin

from django.contrib import admin
from django.apps import apps


# Imports models so to register them to admin
Category = apps.get_model('products', 'Category')
Product = apps.get_model('products', 'Product')
Subcategory = apps.get_model('products', 'Subcategory')



 # Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'old_price', 'price',)
	prepopulated_fields = {'slug': ('name',)}


# Register models to admin panel
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Subcategory, MPTTModelAdmin)



