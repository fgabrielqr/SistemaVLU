from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Book, Category
# Create your views here.

class BookListView(generic.ListView):
    model = Book
    template_name = 'catalog/book_list.html'
    paginate_by = 3

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