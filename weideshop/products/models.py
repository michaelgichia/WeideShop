# -*- coding: utf-8 -*-

# Third Party Stuff
from django.db.models import Model, CharField, ForeignKey, BooleanField, Manager, TextField, DateTimeField, ImageField, DecimalField, PositiveIntegerField, ManyToManyField
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify


# Create your models here.
class ActiveCategoryManager(Manager):
	"""
	A manager that returns active categories.
	"""
	def active(self):
		"""
		Filters categories that are active
		"""
		return self.get_queryset().filter(active=True)


class Category(Model):
	"""
	This is the high level in the product system. It describe how 
	products category are stored.
	E.g Watches, Clothes, Mobile phones e.t.c
	"""
	name = CharField(max_length=50, 
		unique=True)

	parent = ForeignKey('self', 
		null=True, 
		blank=True, 
		related_name='children', 
		db_index=True)

	category_slug = AutoSlugField(max_length=255,
		populate_from=('name'), 
		unique=True,
		help_text=_('A short label, generally used in URLs.'))

	is_active = BooleanField(default=True, 
		verbose_name=_('active'))
	
	objects = Manager()
	active = ActiveCategoryManager()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'categories'
		ordering = ['name']

	def get_absolute_url(self):
		return reverse('category-detail', kwargs={'category_slug': self.category_slug, 'pk': self.id})


class Subcategory(Model):
	"""
	Model class describing category of products.
	"""
	name = CharField(max_length=100, 
		unique=True)

	category = ForeignKey(Category)
	subcategory_slug = AutoSlugField(max_length=255,
		populate_from=('name'), 
		unique=True,
		help_text=_('A short label, generally used in URLs.'))

	description = TextField(blank=True)
	date_created = DateTimeField(_('Date created.'), 
		auto_now_add=True)

	date_updated = DateTimeField(auto_now=True)
	meta_keywords = CharField(max_length=255,
		blank=True,
		help_text=_('Tell search engines what the' 
					'topic of the page is.'))
	# Managers
	objects = Manager()

	def __str__(self):
		return  self.name

	class Meta:
		verbose_name_plural = 'sub-category'
		ordering = ['name']

	def get_absolute_url(self):
		return reverse('sub-category-detail', kwargs={'subcategory_slug': self.subcategory_slug, 'pk': self.id})


class ActiveProductManager(Manager):
	"""
	A manager that returns active products.
	"""
	def active(self):
		"""
		Filters categories that are active
		"""
		return self.get_queryset().filter(active=True)


class FeaturedProductManager(Manager):
	""""
	A manager that returns featured and also active products.
	"""
	def featured(self):
		"""
		Filter featured products.
		"""
		context = self.get_query_set().filter(is_active=True)
		context = context.filter(is_featured=True)
		return context


class OfferProductManager(Manager):
	"""
	This manager class returns products that are in offer.
	"""
	def offer(self):
		context = self.get_query_set().filter(is_active=True)
		context = context.filter(is_offer=True)
		return context


class Product(Model):
	"""
	This model describes the products.
	"""
	name = CharField(max_length=255, 
		unique=True)

	product_slug = AutoSlugField(max_length=255,
		populate_from=('name'), 
		unique=True,
		help_text=_('A short label, generally used in URLs.'))

	image = ImageField(upload_to='photos',
		verbose_name=_('product'))

	caption = CharField(max_length=255,
		blank=True,
		help_text=_('This is a short description on thumbnail'))

	description = TextField(_('description'), 
		blank=True)

	quantity = PositiveIntegerField(null=True, 
		default=0)

	old_price = DecimalField(null=True,
		max_digits=10, 
		decimal_places=2, 
		blank=True)

	price = DecimalField(null=True,
		max_digits=10, 
		decimal_places=2, 
		blank=True)

	is_active = BooleanField(default=True, 
		verbose_name=_('active'))

	is_featured = BooleanField(default=False,
		verbose_name=_('in offer'))

	is_offer = BooleanField(default=False,
		verbose_name=_('featured'),
		help_text=_('Will display as product in offer.'))

	date_created = DateTimeField(_("Date created"), 
						auto_now_add=True)

	date_updated = DateTimeField(auto_now=True)
	sub_category = ManyToManyField(Subcategory)

	# Managers
	objects = Manager()
	active = ActiveProductManager()
	featured = FeaturedProductManager()
	offer = OfferProductManager()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'products'
		ordering = ['-date_created']

	def get_absolute_url(self):
		return reverse('product-detail', kwargs={'product_slug': self.product_slug, 'pk': self.id})	

