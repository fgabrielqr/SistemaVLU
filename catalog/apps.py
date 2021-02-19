from django.apps import AppConfig
from watson import search as watson

class CatalogConfig(AppConfig):
    name = 'catalog'
    verbose_name = 'Catálogo'

    def ready(self):
        Book = self.get_model('Book')
        watson.register(Book)