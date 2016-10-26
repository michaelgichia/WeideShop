
from django.db import models
from django.utils.translation import ugettext_lazy as _



# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=255, unique=True)
	slug = models.CharField(max_length=60)	
	old_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True,default=0.00)
	price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0.00)
	photo = models.FileField(upload_to='photos')
	is_offer = models.BooleanField(default=False)
	is_featured = models.BooleanField(default=False)
	date_created = models.DateTimeField(_("Date created"), auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	description = models.TextField(blank=True)

	class Meta:
		verbose_name_plural = 'products'

	def __str__(self):
		return u"%s" % self.name 


