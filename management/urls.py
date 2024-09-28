from django.urls import path
from . import views

urlpatterns = [
    path('roles/', views.role_list, name='role_list'),
    path('roles/add/', views.add_role, name='add_role'),
]
