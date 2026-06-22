from django.urls import path

from .views import *


urlpatterns = [
    path('ads/',Adlist.as_view(),name='ads_list'),
    # تحديد الإعلان المطلوب باستخدام الـ ID
    path('ads/<int:pk>/',AdDetail.as_view(),name='ad_detail'),
    path('ads/sponsored/',Adsponsored.as_view(),name='sponsored_ad'),
    path('ad/popular/',AdPopular.as_view(),name='ad_popular'),
    
]