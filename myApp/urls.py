from django.urls import path
from . import views

urlpatterns = [
    path('', views.msg, name='index'),
]
