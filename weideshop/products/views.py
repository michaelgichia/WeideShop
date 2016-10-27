from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils import timezone

from .models import Product 

# Create your views here.
class CatalogueListView(ListView):
	'''List all products'''

	model = Product

	def get_context_data(self, **kwargs):
		context = super(CatalogueListView, self).get_context_data(**kwargs)
		return context

class ProductDetailView(DetailView):

	model = Product

