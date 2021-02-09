# coding=utf-8

from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('alterarDados/', views.update_user, name='update_user'),
    path('alterarSenha/', views.update_password, name='update_password'),
    path('cadastro/', views.register, name='register'),
]
