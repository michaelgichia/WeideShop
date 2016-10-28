from django.contrib import admin
from django.apps import apps


# Imports models so to register them to admin
Category = apps.get_model('products', 'Category')
Product = apps.get_model('products', 'Product')


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'date_created', 'date_updated')
	list_per_page = 30
	ordering = ['title']
	search_fields = ['title', 'description', 'meta_keywords']
	prepopulated_fields = {'slug': ('title',),}

# Register models to admin panel
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'is_active', 'is_featured', 
					'is_offer', 'date_created', 'date_updated')
	list_per_page = 30
	ordering = ['-date_created']
	search_fields = ['name', 'description', 'meta_keywords']
	prepopulated_fields = {'slug': ('name',),}

# Register models to admin panel
admin.site.register(Product, ProductAdmin)




