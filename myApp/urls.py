from django.contrib import admin
from django.urls import path, include
from . import views

from catalog import urls as catalog_urls
from catalog import views as views_catalog

urlpatterns = [
    path('', views.index, name='index'),
    path('livro/', views.book, name='book'),
    path('livros/', include('catalog.urls', namespace='catalog')),
    path('contato/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
]
