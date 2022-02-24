from django.contrib import admin
from django.urls import path, include
from .views import product_view, addproduct_view

urlpatterns = [
    path('', product_view),
    path('addproduct/', addproduct_view),
]
