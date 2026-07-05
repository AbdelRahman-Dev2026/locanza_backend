from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from .models import Banner,Slider,HomeCategory
from .serializer import BannerSerializer,SliderSerializer,HomeCategorySerializer

from Ads.models import Ad

from Ads.serializers import  AdListSerializer


class BannerViewSet(ModelViewSet):

    serializer_class = BannerSerializer
    queryset = Banner.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]

        return [IsAuthenticated()]

class SliderViewSet(ModelViewSet):
    serializer_class = SliderSerializer
    queryset = Slider.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]

        return [IsAuthenticated()]


class HomeCategoryViewSet(ModelViewSet):

    serializer_class = HomeCategorySerializer
    queryset = HomeCategory.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]

        return [IsAuthenticated()]

class CoreView(APIView):
    def get(self, request):

        benners = Banner.objects.filter(is_active=True)

        sliders = Slider.objects.filter(is_active=True)
        categories = HomeCategory.objects.filter(is_active=True)
        sponsors = Ad.objects.filter(is_active=True,ad_status='sponsored')
        featured = Ad.objects.filter(is_active=True,).order_by('-created_at')
        
        popular = Ad.objects.filter(is_active=True,).order_by('-quantity')

        data = {
            "banners": BannerSerializer(benners, many=True).data,
            "sliders": SliderSerializer(sliders, many=True).data,
            "categories": HomeCategorySerializer(categories, many=True).data,
            "sponsored_ads": AdListSerializer(sponsors, many=True).data,
            "featured_ads": AdListSerializer(featured, many=True).data,
            "popular_ads": AdListSerializer(popular, many=True).data,
        }
        return Response(data)










# Create your views here.
