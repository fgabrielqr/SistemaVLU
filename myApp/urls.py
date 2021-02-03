from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listarLivros/', views.book_list, name='book_list'),
    path('livro/', views.book, name='book'),
    path('contato/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
]
