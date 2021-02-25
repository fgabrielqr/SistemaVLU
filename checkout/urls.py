from django.urls import path, re_path, include
from rest_framework import routers
from . import views
from .api.viewset import CartItemViewSet, OrderViewSet, OrderItemViewSet
from .views import OrderLisDelete

router = routers.DefaultRouter()
router.register(r'carts', CartItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'ordersItems', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('excluirPedido/<int:pk>/', OrderLisDelete.as_view(), name='orderLisDelete'),
    re_path('^carrinho/adicionar/(?P<slug>[\w_-]+)/$', views.create_cartitem, name='create_cartitem'),
    path('carrinho/', views.cart_item, name='cart_item'),
    path('finalizando/', views.checkout, name='checkout'),
    re_path('^finalizando/(?P<pk>\d+)/paypal/$', views.paypal_view,
        name='paypal_view'),
    path('meusPedidos/', views.order_list, name='order_list'),
    re_path('^meusPedidos/(?P<pk>\d+)/$', views.order_detail, name='order_detail'),
]
