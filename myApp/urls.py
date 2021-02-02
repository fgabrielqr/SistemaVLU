from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', views.book_list, name='book_list'),
    path('book/', views.book, name='book'),
    path('contact/', views.contact, name='contact'),
]
