from django.views.generic.edit import CreateView #UpdateView
from catalog.models import Book, Category
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Create
class CategoryCreate(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login')
    model = Category
    fields = ['name', 'slug']
    template_name = 'register/form.html'
    success_url = reverse_lazy('index')

class BookCreate(LoginRequiredMixin ,CreateView):
    login_url = reverse_lazy('login')
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

