from django.urls import path

from .views import *


urlpatterns = [
    path('orders/', OrdersNormalView.as_view(), name='orders-list-create'),
    path('orders/<int:pk>/', OrdersDetailView.as_view(), name='orders-detail'),
]
