from django.urls import path

from .views import ReviewsView

urlpatterns = [
    path('api_review/', ReviewsView.as_view(), name='review'),
]