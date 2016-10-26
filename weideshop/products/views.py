from django.shortcuts import render
from django.views.generic import ListView
from django.utils import timezone

from .models import Product 

# Create your views here.
class CatalogueListView(ListView):

	model = Product

	def get_context_data(self, **kwargs):
		context = super(CatalogueListView, self).get_context_data(**kwargs)
		return context
