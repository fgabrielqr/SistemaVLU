"""SistemaVLU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from catalog.views import BookViewSet, CategoryViewSet
from accounts.views import UserViewSet
from checkout.views import CartItemViewSet, OrderViewSet, OrderItemViewSet
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='My Swagger API Documentation')

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'categorys', CategoryViewSet)
router.register(r'users', UserViewSet)
router.register(r'carts', CartItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'ordersItems', OrderItemViewSet)

urlpatterns = [
    path('', include('myApp.urls')),
    path('catalogo/', include('catalog.urls')),
    path('conta/', include('accounts.urls')),
    path('compras/', include('checkout.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('cadastro/', include('register.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )