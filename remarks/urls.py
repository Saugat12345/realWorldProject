from django.contrib import admin
from django.urls import path, include
from .views import remarkpage_view

urlpatterns = [
    path('', remarkpage_view),
]