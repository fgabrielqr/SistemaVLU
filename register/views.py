from django.views.generic.edit import CreateView #UpdateView
from catalog.models import Book, Category
from django.urls import reverse_lazy


# Create
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

# Update
#class CategoryUpdate(UpdateView):
#    model = Category
#    fields = ['name', 'slug']
#    template_name = 'register/form.html'
#    success_url = reverse_lazy('index')

#class BookUpdate(UpdateView):
#   model = Book
#   fields = ['name', 'slug', 'category', 'description', 'price', 'image']
#   template_name = 'register/form.html'
#   success_url = reverse_lazy('index')

