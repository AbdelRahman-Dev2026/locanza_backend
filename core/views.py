from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import Banner,Slider,HomeCategory
from .serializer import BannerSerializer,SliderSerializer,HomeCategorySerializer


class BannerListCreateView(ListCreateAPIView):

    permission_classes = [IsAdminUser]
    serializer_class = BannerSerializer
    def get_queryset(self):
        return Banner.objects.filter(is_active=True)


class BannerDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Banner.objects.all()

    serializer_class = BannerSerializer
    permission_classes = [IsAdminUser]


class SliderListCreateView(ListCreateAPIView):

    permission_classes = [IsAdminUser]
    serializer_class = SliderSerializer
    def get_queryset(self):
        return Slider.objects.filter(is_active=True)


class SliderDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    permission_classes = [IsAdminUser]

class HomeCategoryListCreateView(ListCreateAPIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny(), ]

        if self.request.method == 'POST':
            return [IsAdminUser, ]

    serializer_class = HomeCategorySerializer

    def get_queryset(self):
        return HomeCategory.objects.filter(is_active=True)


class HomeCategoryDetailView(RetrieveUpdateDestroyAPIView):

    queryset = HomeCategory.objects.all()
    serializer_class = HomeCategorySerializer
    permission_classes = [IsAdminUser]



# Create your views here.
