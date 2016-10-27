from mptt.models import MPTTModel, TreeForeignKey

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


# Create your models here.
class Category(MPTTModel):
	name = models.CharField(max_length=50, unique=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

	class MPTTMeta:
		order_insertion_by = ['name']


class Subcategory(models.Model):
	name = models.CharField(max_length=100, unique=True)
	child = models.ForeignKey(Category)

	class MPTTMeta:
		order_insertion_by = ['name']


class Product(models.Model):
	name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(help_text="A short label, generally used in URLs.")
	category = models.ManyToManyField(Subcategory)
	old_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True,default=0.00)
	price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0.00)
	photo = models.ImageField(max_length=100,
							upload_to='photos',
							verbose_name=_('product'))
	is_offer = models.BooleanField(default=False,
									help_text=_('Will display as offer product.'))
	is_featured = models.BooleanField(default=False)
	date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	description = models.TextField(_('description'), blank=True)


	class Meta:
		verbose_name_plural = 'products'

	def get_absolute_url(self):
		return reverse('detail', kwargs={'slug': self.slug})

	def __str__(self):
		return self.name	


