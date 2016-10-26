from django.contrib import admin
from django.apps import apps

# Register your models here.
Product = apps.get_model('products', 'Product')


class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)