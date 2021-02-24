# coding=utf-8
from rest_framework import routers
from django.urls import path, include
from .api.viewset import UserViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('alterarDados/', views.update_user, name='update_user'),
    path('alterarSenha/', views.update_password, name='update_password'),
    path('cadastro/', views.register, name='register'),
    path('', include(router.urls)),
]
