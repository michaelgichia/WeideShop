from django.conf.urls import url, include
from .views import CatalogueListView


urlpatterns = [
    url(r'^$', CatalogueListView.as_view(), name='gallery'),
   
] 