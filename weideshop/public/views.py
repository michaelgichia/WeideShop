from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
	'''This class displays the landing page.'''
	
	template_name = 'index.html'