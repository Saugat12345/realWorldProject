from django.urls.resolvers import URLPattern
from . import views
from django.urls import path, include
from .views import workers_view, addworker_view

urlpatterns = [
    path('', workers_view),
    path('addworker/', addworker_view),
]