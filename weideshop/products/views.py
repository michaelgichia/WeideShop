from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from .models import Product, Subcategory, Category 


class CategoryListView(ListView):
	"""
	Browse all products in the categories.
	"""
	models = Category
	template_name = 'products/category_list.html'

	def get_queryset(self):
		"""
		Returns all categories.
		"""
		return Category.objects.get_queryset().all()


class SubcategoryListView(ListView):
	"""
	Browse all products in the sub-catalogue.
	"""
	model = Subcategory
	template_name = 'products/subcategory_list.html'

	def get_queryset(self):
		"""
		Returns all sub-categories.
		"""
		self.category = get_object_or_404(Category, slug = self.kwargs.get('slug'))
		return Subcategory.objects.filter(category = self.category)


class ProductListView(ListView):
	"""
	Return products according to previous selected subcategory.
	"""
	model = Product

	def get_queryset(self):
		"""
		Display all products under selected subcategory.
		"""
		self.subcategory = get_object_or_404(Subcategory, subcategory_slug = self.kwargs.get('subcategory_slug'))
		return Product.objects.filter(subcategory=self.subcategory)


class CatalogueListView(ListView):
	"""
	Display all products in the db.
	"""
	model = Product

	def get_queryset(self):
		"""
		Returns all categories.
		"""
		return Product.objects.get_queryset().all()
		

class CatalogueDetailView(DetailView):
	"""
	Display individual products details
	"""
	model = Product
	template_name = 'products/product_detail.html'
	slug_field = 'product_slug'

	def get_object(self):
		# Call the superclass
		object = super(CatalogueDetailView, self).get_object()
		return object


	# model = Product
	# template_name = 'products/product_detail.html'
	# slug_field = 'product_slug'



