
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


# Create your models here.
class Category(models.Model):
	"""
	Model class describing category of products.
	"""
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=50, 
							unique=True,
							help_text=_('A short label, generally used in URLs.'))
	description = models.TextField()
	date_created = models.DateTimeField(_("Date created."), auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	meta_keywords = models.CharField(max_length=255,
									help_text=_('Tell search engines what the topic of the page is.'))
	# Managers
	objects = models.Manager()

	class Meta:
		verbose_name_plural = 'categories'
		ordering = ['title']

	def __str__(self):
		return '%s' % self.title

	def get_absolute_url(self):
		return reverse('category_catalog', kwargs={'slug': self.slug})


class ActiveProductManager(models.Manager):
	"""This manager class returns Active products."""
	def get_query_set(self):
		return super(ActiveProductManager, self).get_query_set().filter(is_active=True)


class FeaturedProductManager(models.Manager):
	""""This manager class returns featured products and is active."""
	def get_query_set(self):
		return super(FeaturedProductManager, self).get_query_set().filter(is_active=True).filter(is_featured=True)


class OfferProductManager(models.Manager):
	"""This manager class returns products that are in offer."""
	def get_query_set(self):
		return super(OfferProductManager, self).get_query_set().filter(is_active=True).filter(is_offer=True)


class Product(models.Model):
	"""
	This model describes the products.
	"""
	name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(max_length=100, 
							unique=True,
							help_text=_('A short label, generally used in URLs.'))
	image = models.ImageField(max_length=100,
							upload_to='photos',
							verbose_name=_('product'))
	thumbnail_caption = models.CharField(max_length=255)
	description = models.TextField(_('description'), blank=True)
	quantity = models.PositiveIntegerField(blank=True)	
	old_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
	price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
	is_active = models.BooleanField(default=True)
	is_featured = models.BooleanField(default=False)
	is_offer = models.BooleanField(default=False,
									help_text=_('Will display as product in offer.'))
	date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	category = models.ManyToManyField(Category)
	# Managers
	objects = models.Manager()
	active = ActiveProductManager()
	featured = FeaturedProductManager()
	offer = OfferProductManager()

	class Meta:
		verbose_name_plural = 'products'
		ordering = ['-date_created']

	def __str__(self):
		return '%s' % self.name

	def get_absolute_url(self):
		return reverse('detail', kwargs={'slug': self.slug})	


