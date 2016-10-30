from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from mptt.managers import TreeManager

# Create your models here.
class ActiveCategoryManager(models.Manager):
	"""
	A manager that returns active categories.
	"""
	def active(self):
		"""
		Filters categories that are active
		"""
		return self.get_queryset().filter(active=True)

class Category(MPTTModel):

	parent = TreeForeignKey(
		'self',
		blank=True,
		null=True,
		related_name='children',
		verbose_name=_('parent'))

	name = models.CharField(max_length=100, 
		verbose_name=_('name'))

	slug = models.SlugField(max_length=50, 
		unique=True,
		help_text=_('A short label, generally used in URLs.'))

	is_active = models.BooleanField(default=True, 
		verbose_name=_('active'))

	active = ActiveCategoryManager()
	tree = TreeManager()

	class Meta:
		verbose_name_plural = 'categories'
		ordering = ['name']

	class MPTTMeta:
		order_insertion_by = ('name',)

	def __str__(self):
		return '%s' % self.name 

	def get_absolute_url(self):
		return reverse('category', kwargs={'slug': self.slug})


class Subcategory(models.Model):
	"""
	Model class describing category of products.
	"""
	name = models.CharField(max_length=100, 
		unique=True)

	category = models.ForeignKey(Category)
	slug = models.SlugField(max_length=50, 
		unique=True,
		help_text=_('A short label, generally used in URLs.'))

	description = models.TextField()
	date_created = models.DateTimeField(_('Date created.'), 
		auto_now_add=True)

	date_updated = models.DateTimeField(auto_now=True)
	meta_keywords = models.CharField(max_length=255,
		help_text=_('Tell search engines what the' 
					'topic of the page is.'))
	# Managers
	objects = models.Manager()

	class Meta:
		verbose_name_plural = 'sub-categories'
		ordering = ['name']

	def __str__(self):
		return '%s' % self.name

	def get_absolute_url(self):
		return reverse('category_list', kwargs={'slug': self.slug})


class ActiveProductManager(models.Manager):
	"""
	A manager that returns active products.
	"""
	def active(self):
		"""
		Filters categories that are active
		"""
		return self.get_queryset().filter(active=True)


class FeaturedProductManager(models.Manager):
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


class OfferProductManager(models.Manager):
	"""
	This manager class returns products that are in offer.
	"""
	def offer(self):
		context = self.get_query_set().filter(is_active=True)
		context = context.filter(is_offer=True)
		return context


class Product(models.Model):
	"""
	This model describes the products.
	"""
	name = models.CharField(max_length=255, 
				unique=True)

	slug = models.SlugField(max_length=100, 
				unique=True,
				help_text=_('A short label, generally used in URLs.'))

	image = models.ImageField(max_length=100,
				upload_to='photos',
				verbose_name=_('product'))

	thumbnail_caption = models.CharField(max_length=255)
	description = models.TextField(_('description'), 
					blank=True)

	quantity = models.PositiveIntegerField(null=True, 
					default=0)

	old_price = models.DecimalField(max_digits=9, 
					decimal_places=2, 
					blank=True)

	price = models.DecimalField(max_digits=6, 
				decimal_places=2, 
				blank=True)

	is_active = models.BooleanField(default=True, 
		verbose_name=_('active'))

	is_featured = models.BooleanField(default=False,
		verbose_name=_('in offer'))

	is_offer = models.BooleanField(default=False,
		verbose_name=_('featured'),
		help_text=_('Will display as product in offer.'))

	date_created = models.DateTimeField(_("Date created"), 
						auto_now_add=True)

	date_updated = models.DateTimeField(auto_now=True)
	sub_category = models.ManyToManyField(Subcategory)

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

