# /part_django/part/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item_parts/', views.item_part_list, name='item_part_list')
]