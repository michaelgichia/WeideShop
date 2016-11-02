from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.utils import timezone

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
	Browse all products in the catalogue.
	"""
	model = Subcategory
	template_name = 'products/subcategory_list.html'

	def get_queryset(self):
		"""
		Returns all sub-categories.
		"""
		category = get_object_or_404(Category, slug = self.kwargs.get('slug'))
		return Subcategory.objects.filter(category = category)


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
		

class ProductDetailView(DetailView):
	"""
	Display individual products details
	"""

	model = Product

