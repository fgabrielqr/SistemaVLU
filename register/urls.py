from django.urls import path
from .views import CategoryCreate, BookCreate

urlpatterns = [
    path('categoria/', CategoryCreate.as_view(), name='registerCategory'),
    path('livro/', BookCreate.as_view(), name='registerBook'),
]