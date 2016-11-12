from weideshop.products.models import Category
import factory

class CategoryFactory(factory.Factory):
	class Meta:
		model = Category

	name = 'clothes'
	category_slug = 'clothes'