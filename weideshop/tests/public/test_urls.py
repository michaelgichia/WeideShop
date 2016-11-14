from django.test import TestCase
from django.core.urlresolvers import resolve, reverse

from weideshop.public.views import IndexView

class TestPublicURLs(TestCase):

	def test_root_url_uses_index_view(self):
		"""
		Test that the CategoryListView() uses
		'/'
		"""

		root = resolve('/')
		self.assertEqual(root.func.__name__, 'IndexView')

