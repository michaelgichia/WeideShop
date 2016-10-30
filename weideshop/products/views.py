from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.utils import timezone

from .models import Product, Subcategory 

# Create your views here.
class SubcategoryListView(ListView):
	"""
	Browse all products in the catalogue.
	"""
	model = Subcategory

	def get_context_data(self, **kwargs):
		context = super(SubcategoryListView, self).get_context_data(**kwargs)
		context['title'] = Subcategory.objects.all()
		context['description'] = Subcategory.objects.all()
		return context

class CatalogueListView(ListView):
	'''List all products'''

	model = Product

	def get_context_data(self, **kwargs):
		context = super(CatalogueListView, self).get_context_data(**kwargs)
		return context

class ProductDetailView(DetailView):

	model = Product

