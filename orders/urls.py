from django.contrib import admin
from django.urls import path, include
from .views import order_view, trade_agreement_view, automobileorder_view, workerorder_view

urlpatterns = [
    path('', order_view),
    path('tradeagreement/', trade_agreement_view),

    path('finalize/<int:pd_id>', order_view, name='finalize'),
    path('finalizeautomobile/<int:am_id>', automobileorder_view, name='finalizeautomobile'),
    path('finalizeworker/<int:wr_id>', workerorder_view, name='finalizeworker'),
]
