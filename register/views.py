from django.views.generic.edit import CreateView
from catalog.models import Book, Category
from django.urls import reverse_lazy


# Create your views here.
class CategoryCreate(CreateView):
    model = Category
    fields = ['name', 'slug']
    template_name = 'register/form.html'
    success_url = reverse_lazy('index')

class BookCreate(CreateView):
    model = Book
    fields = ['name', 'slug', 'category', 'description', 'price', 'image']
    template_name = 'register/form.html'
    success_url = reverse_lazy('index')