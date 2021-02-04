from django.urls import path
from . import views

urlpatterns = {
    path('livros/', views.book_list, name='book_list'),
}