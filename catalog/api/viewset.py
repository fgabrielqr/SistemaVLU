from .serializers import BookSerializer, CategorySerializer
from rest_framework import viewsets
from catalog.models import Book, Category

# API
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = CategorySerializer