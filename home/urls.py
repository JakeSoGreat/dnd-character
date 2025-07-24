from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.custom_login, name='custom_login'),
    path('register/', views.register, name='register'),
    path('', views.home_page_view, name='home'),

    # Character CRUD
    path('characters/', views.character_list, name='character_list'),
    path('characters/create/', views.character_create, name='character_create'),
    path('characters/<int:pk>/edit/', views.character_update, name='character_update'),
    path('characters/<int:pk>/delete/', views.character_delete, name='character_delete'),
]
