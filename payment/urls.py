from django.urls import path

from .views import PaymentView,PaymentDetailView


urlpatterns = [
    path('payment/', PaymentView.as_view(),name='payment_list'),
    path('payment/<int:pk>/',PaymentDetailView.as_view(),name='payment_detail'),


]