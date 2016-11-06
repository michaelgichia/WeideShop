from django.conf.urls import url, include

from .views import CategoryListView, SubcategoryListView, ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
	url(r'^$', CategoryListView.as_view(), name='categories'),
    url(r'^(?P<category_slug>[-\w]+)/$', SubcategoryListView.as_view(), name='sub-category'),
	url(r'^(?P<category_slug>[-\w]+)/(?P<subcategory_slug>[-\w]+)/$', ProductListView.as_view(), name='product-list'),
	url(r'^(?P<category_slug>[-\w]+)/(?P<subcategory_slug>[-\w]+)/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product-detail'),

] 
