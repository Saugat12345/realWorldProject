from django.contrib import admin
from django.urls import path, include
from .views import wishlist_view, save_automobilewishlist, save_productwishlist, \
    delete_automobilewish, delete_productwish, order_automobilewish, order_productwish

from orders.views import order_view, automobileorder_view

urlpatterns = [
    path('', wishlist_view),
    path('saveproductwishlist/<int:pd_id>', save_productwishlist, name='saveproductwishlist'),
    path('saveautomobilewishlist/<int:am_id>', save_automobilewishlist, name='saveautomobilewishlist'),

    # Urls to delete wishes
    path('deleteproductwish/<int:wish_id>', delete_productwish, name='deleteproductwish'),
    path('deleteautomobilewish/<int:wish_id>', delete_automobilewish, name='deleteautomobilewish'),

    #Urls to order wishes
    path('finalize/<int:pd_id>', order_productwish, name='finalize'),
    path('finalizeautomobile/<int:am_id>', order_automobilewish, name='finalizeautomobile'),

]
