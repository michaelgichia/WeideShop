import factory

from weideshop.products.models import Category


class CategoryFactory(factory.Factory):
	class Meta:
		model = Category

	name = factory.Sequence(lambda n: 'category%d' % n)
	category_slug = name
