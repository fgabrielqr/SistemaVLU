from django.shortcuts import render
from .models import Book
# Create your views here.

def book_list(request):
    context = {
        'book_list': Book.objects.all()
    }
    return render(request, 'catalog/book_list.html', context)