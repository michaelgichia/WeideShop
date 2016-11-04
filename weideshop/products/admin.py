from django.contrib import admin
from django.apps import apps


# Imports models so to register them to admin
Category = apps.get_model('products', 'Category')
Subcategory = apps.get_model('products', 'Subcategory')
Product = apps.get_model('products', 'Product')


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')
	list_per_page = 30
	ordering = ['name']
	search_fields = ['name',]
	prepopulated_fields = {'slug': ('name',),}

# Register models to admin panel
admin.site.register(Category,CategoryAdmin)

class SubcategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'date_created', 'date_updated')
	list_per_page = 30
	ordering = ['name']
	search_fields = ['name', 'description', 'meta_keywords']
	prepopulated_fields = {'subcategory_slug': ('name',),}

# Register models to admin panel
admin.site.register(Subcategory, SubcategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'is_active', 'is_featured', 
					'is_offer', 'date_created', 'date_updated')
	list_per_page = 30
	ordering = ['-date_created']
	search_fields = ['name', 'description', 'meta_keywords']
	prepopulated_fields = {'product_slug': ('name',),}

# Register models to admin panel
admin.site.register(Product, ProductAdmin)




