# coding=utf-8
from django.test import TestCase, Client
from django.urls import reverse
from model_mommy import mommy

from catalog.models import Category, Book


class BookListTestCase(TestCase):
    def setUp(self):
        self.url = reverse('book_list')
        self.client = Client()
        self.book = mommy.make('catalog.Book', _quantity=10)

    def tearDown(self):
        Book.objects.all().delete()

    def test_view_ok(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/book_list.html')

    def test_context(self):
        response = self.client.get(self.url)
        self.assertTrue('book_list' in response.context)
        book_list = response.context['book_list']
        self.assertEquals(book_list.count(), 3)
        paginator = response.context['paginator']
        self.assertEquals(paginator.num_pages, 4)

    def test_page_not_found(self):
        response = self.client.get('{}?page=5'.format(self.url))
        self.assertEquals(response.status_code, 404)