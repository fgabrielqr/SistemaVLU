from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contact, name='contact'),
    path('termoos/', views.privacy, name='privacy'),
    path('entrar/', LoginView.as_view(template_name='login.html'), name='login'),
    path('sair/', LogoutView.as_view(next_page='index'), name='logout'),
]


