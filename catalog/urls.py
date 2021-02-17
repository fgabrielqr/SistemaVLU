from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    re_path('^(?P<slug>[\w_-]+)/$', views.category, name='category'),
    re_path('^livros/(?P<slug>[\w_-]+)/$', views.book, name='book'),

]

