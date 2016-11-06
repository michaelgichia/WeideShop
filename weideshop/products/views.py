# -*- coding: utf-8 -*-

# Third party stuff
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

# Our stuff
from .models import Product, Subcategory, Category 


class CategoryListView(ListView):
	"""
	Browse all products in the categories.
	"""
	models = Category
	template_name = 'products/category_list.html'
	context_object_name = "Category list"

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
	context_object_name = "Sub-Category list"
	category_model = Category

	def get_queryset(self):
		"""
		Returns all sub-categories.
		"""
		self.category = get_object_or_404(Category, category_slug = self.kwargs.get('category_slug'))
		return Subcategory.objects.filter(category = self.category)

	def get_context_data(self, **kwargs):
		"""
		Returns self.category_slug needed 
		on the subcategory_list.html as a
		one of the {% url %} slug params.
		"""
		context = super(SubcategoryListView, self).get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		context['category_slug'] = self.kwargs.get('category_slug')
		return context


class ProductListView(ListView):
	"""
	Browse products according to previous selected subcategory.
	"""
	model = Product
	template_name = 'products/product_list.html'
	context_object_name = "Product list"

	def get_context_data(self, **kwargs):
		"""
		Returns self.category_slug and self.subcategory)slug needed 
		on the product_list.html as a
		one of the {% url %} slug params.
		"""
		context = super(ProductListView, self).get_context_data(**kwargs)
		# Get category_slug
		context['categories'] = Category.objects.all()
		context['category_slug'] = self.kwargs.get('category_slug')
		# Get subcategory_slug
		context['subcategories'] = Subcategory.objects.all()
		context['subcategory_slug'] = self.kwargs.get('subcategory_slug')
		return context

	def get_queryset(self):
		"""
		Browse all products under selected subcategory.
		"""
		self.sub_category = get_object_or_404(Subcategory, subcategory_slug = self.kwargs.get('subcategory_slug'))
		return Product.objects.filter(sub_category = self.sub_category)


class ProductDetailView(DetailView):
	"""
	Display individual products details
	"""
	model = Product

	def get_object(self):
		object = get_object_or_404(Product, product_slug=self.kwargs['product_slug'])
		return object 
	

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
		"""
		Call the superclass
		"""
		object = super(CatalogueDetailView, self).get_object()
		return object

	



