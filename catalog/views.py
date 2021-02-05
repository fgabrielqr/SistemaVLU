from django.shortcuts import render
from .models import Book, Category
# Create your views here.

def book_list(request):
    context = {
        'book_list': Book.objects.all()
    }
    return render(request, 'catalog/book_list.html', context)

def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category': category,
        'book_list': Book.objects.filter(category=category),
    }
    return render(request, 'catalog/category.html', context)

def book(request, slug):
    book = Book.objects.get(slug=slug)
    context = {
        'book': book
    }
    return render(request, 'catalog/book.html', context)