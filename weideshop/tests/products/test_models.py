# Third party stuff
from django.test import TestCase

# Our stuff
from weideshop.products.models import Category, Subcategory, Product 
from weideshop.tests.factories.products import CategoryFactory

class CategoryModelTest(TestCase):

	def test_saving_and_retrieving_category(self):
		first_cats = Category()
		first_cats.name = 'Clothes'
		first_cats.category_slug = (first_cats.name).lower
		first_cats.save()

		saved_cats = Category.objects.all()
		self.assertEqual(saved_cats.count(), 1)
