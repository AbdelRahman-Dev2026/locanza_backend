from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()

router.register('banners', BannerViewSet)
router.register('sliders', SliderViewSet)
router.register('home-categories', HomeCategoryViewSet)

urlpatterns = [
    path('home/', CoreView.as_view(), name='core-home-page'),
]

urlpatterns += router.urls

