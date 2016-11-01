from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.utils import timezone

from .models import Product, Subcategory, Category 

# Create your views here.
class CategoryListView(ListView):
	"""
	Browse all products in the categories.
	"""
	models = Category

	def get_queryset(self, **kwargs):
		
		return Category.objects.get_queryset().all()


class SubcategoryListView(ListView):
	"""
	Browse all products in the catalogue.
	"""
	model = Subcategory

	def get_queryset(self, **kwargs):
		return Subcategory.objects.get_queryset().all()


class CatalogueListView(ListView):
	'''List all products'''

	model = Product

	def get_context_data(self, **kwargs):
		context = super(CatalogueListView, self).get_context_data(**kwargs)
		return context

class ProductDetailView(DetailView):

	model = Product

