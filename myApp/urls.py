from django.urls import path
from . import views

from catalog import urls as catalog_urls
from catalog import views as views_catalog

urlpatterns = [
    path('', views.index, name='index'),
    path('livro/', views.book, name='book'),
    path('contato/', views.contact, name='contact'),
]
