from django.conf.urls import url, include
from .views import CatalogueListView, ProductDetailView, SubcategoryListView, CategoryListView


urlpatterns = [
	url(r'^$', CategoryListView.as_view(), name='category'),
    url(r'^catalog/$', CatalogueListView.as_view(), name='category_catalog'),
    url(r'^(?P<slug>[-\w]+)/$', SubcategoryListView.as_view(), name='sub-category'),   
    url(r'^catalog/(?P<slug>[-\w]+)/$', ProductDetailView.as_view(), name='detail'),
] 