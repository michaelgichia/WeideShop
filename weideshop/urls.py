"""weideshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from weideshop.products.views import CatalogueListView,CatalogueDetailView 
from weideshop.public.views import IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',IndexView.as_view(), name='home'),

    url(r'^catalog/$', CatalogueListView.as_view(), name='catalogue'),
    # url(r'^catalog/(?P<product_slug>[-\w]+)/$', CatalogueDetailView.as_view(), name='detail'),

    url(r'^category/', include('weideshop.products.urls', namespace='products-app', app_name='products')),
    
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        ]