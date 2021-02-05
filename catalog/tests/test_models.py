from django.test import TestCase
from django.urls import reverse
from catalog.models import Category, Book
from model_mommy import mommy

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = mommy.make('catalog.Category')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.category.get_absolute_url(),
            reverse('category', kwargs={'slug': self.category.slug})
        )

class BookTestCase(TestCase):
    def setUp(self):
        self.book = mommy.make(Book, slug='livro')

    def test_get_absolute_url(self):
        self.assertEquals(
            self.book.get_absolute_url(),
            reverse('book', kwargs={'slug': 'livro'})
        )