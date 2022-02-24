from django.contrib import admin
from django.urls import path, include
from .views import automobile_view, addautomobile_view
from orders.views import automobileorder_view

urlpatterns = [
    path('', automobile_view),
    path('addautomobile/', addautomobile_view),
    path('finalizeautomobile/<int:am_id>', automobileorder_view, name='finalizeautomobile'),
]
