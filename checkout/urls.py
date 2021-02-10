from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path('^carrinho/adicionar/(?P<slug>[\w_-]+)/$', views.create_cartitem, name='create_cartitem'),
    path('carrinho/', views.cart_item, name='cart_item'),
    path('finalizando/', views.checkout, name='checkout'),
]
