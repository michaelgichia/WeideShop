from django.test import TestCase
from django.core.urlresolvers import resolve

from weideshop.products.views import CategoryListView

class TestCategoryListViewURLs(TestCase):

	def test_category_list_view_url(self):
		"""
		Test that the CategoryListView() uses
		'/category/'
		"""

		root = resolve('/category/')
		self.assertEqual(root.func.__name__, 'CategoryListView')
