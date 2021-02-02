from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def book_list(request):
    return render(request, 'book_list.html')

def book(request):
    return render(request, 'book.html')

def contact(request):
    return render(request, 'contact.html')