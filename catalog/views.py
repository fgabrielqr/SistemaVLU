from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.db import models
from watson import search as watson
from .models import Book, Category
# Create your views here.

class BookListView(generic.ListView):
    template_name = 'catalog/book_list.html'
    context_object_name = 'books'
    paginate_by = 3

    def get_queryset(self):
        queryset = Book.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = watson.filter(queryset, q)
        return queryset

book_list = BookListView.as_view()

class CategoryListView(generic.ListView):
    template_name = 'catalog/category.html'
    context_object_name = 'book_list'
    paginate_by = 3

    def get_queryset(self):
        return Book.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self,  **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

category = CategoryListView.as_view()

def book(request, slug):
    book = Book.objects.get(slug=slug)
    context = {
        'book': book
    }
    return render(request, 'catalog/book.html', context)