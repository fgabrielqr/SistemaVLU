from django.urls import path, re_path, include
from .api.viewset import BookViewSet, CategoryViewSet
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'categorys', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('livros/', views.book_list, name='book_list'),
    re_path('^(?P<slug>[\w_-]+)/$', views.category, name='category'),
    re_path('^livro/(?P<slug>[\w_-]+)/$', views.book, name='book'),
]

