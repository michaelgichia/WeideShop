from django.conf.urls import url, include
from .views import CatalogueListView, ProductDetailView

urlpatterns = [
    url(r'^$', CatalogueListView.as_view(), name='category_catalog'),
    url(r'^(?P<slug>[-\w]+)/$', ProductDetailView.as_view(), name='detail'),
   
] 