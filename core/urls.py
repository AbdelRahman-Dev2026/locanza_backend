from django.urls import path

from .views import *

urlpatterns = [
    path('banners/',BannerListCreateView.as_view(), name='BannerListCreate'),
    path('banners/<int:pk>/',BannerDetailView.as_view(), name='BannerDetail'),

    path('sliders/',SliderListCreateView.as_view(), name='SliderListCreate'),
    path('sliders/<int:pk>/',SliderDetailView.as_view(), name='SliderDetail'),

    path('home-categories/',HomeCategoryListCreateView.as_view(), name='HomeCategoryListCreate'),
    path('home-categories/<int:pk>/',HomeCategoryDetailView.as_view(), name='HomeCategoryDetail'),
]