from django.contrib import admin
from .models import Book, Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']

class BookAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'category', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)