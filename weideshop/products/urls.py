from django.conf.urls import url, include

from .views import SubcategoryListView, CategoryListView, ProductListView

app_name = 'product-app'

urlpatterns = [
	url(r'^$', CategoryListView.as_view(), name='category'),
    url(r'^(?P<slug>[-\w]+)/$', SubcategoryListView.as_view(), name='sub-category'),
    url(r'^(?P<slug>[-\w]+)/(?P<product_slug>[-\w]+)/$', ProductListView.as_view(), name='product-list'),

] 
