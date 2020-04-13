# /part_django/part/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item_parts/', views.item_part_list, name='item_part_list'),
    path('items/<int:pk>', views.item_detail, name='item_detail'),
    path('item_parts/<int:pk>', views.item_part_detail, name='item_part_detail'),
    path('items/new', views.item_create, name='item_create'),
    path('item_parts/new', views.item_part_create, name='item_part_create'),
    path('items/<int:pk>/edit', views.item_edit, name='item_edit'),
    path('item_parts/<int:pk>/edit', views.item_part_edit, name='item_part_edit'),
]