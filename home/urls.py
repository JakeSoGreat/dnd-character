from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.custom_login, name='custom_login'),
    path('register/', views.register, name='register'),
    path('', views.home_page_view, name='home'),
]
