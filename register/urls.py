from django.urls import path
from .views import CategoryCreate, BookCreate
#from .views import CategoryUpdate, BookUpdate

urlpatterns = [
    path('categoria/', CategoryCreate.as_view(), name='registerCategory'),
    path('livro/', BookCreate.as_view(), name='registerBook'),
    #path('editarLivro/<int:pk>/', BookUpdate.as_view(), name='updateBook'),
    #path('editarCategoria/<int:pk>/', CategoryUpdate.as_view(), name='updateCategory'),
]