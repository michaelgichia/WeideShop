
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=255, unique=True)
	slug = models.SlugField(_('name slug'),
                            unique=True,
                            max_length=250,
                            help_text=_('A "slug" is a unique URL-friendly title for an object.'))	
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

	def __str__(self):
		return self.name	

	def get_absolute_url(self):
		return reverse('catalogue:gallery', args=[self.slug])

