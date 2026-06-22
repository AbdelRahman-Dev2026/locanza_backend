from django.http import Http404
from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .models import Ad
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .seriallizer import AdListSerializer, AdDetailSerializer


class Adlist(APIView):

    # - تحديد صلاحيات الوصول
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]

        return [IsAuthenticated(), IsAdminUser() ]

    # - جلب الإعلانات النشطة
    def get(self,request):
        ads = Ad.objects.filter(
            is_active=True,
        )
        # تحويل البيانات إلى JSON
        serializer  = AdListSerializer(
            ads,
            many=True,
        )
        # - إرجاع البيانات للمستخدم عبر API
        return Response(serializer.data)


    def post(self,request):
        serializer = AdDetailSerializer(
            data=request.data
        )

        # انشاء الاعلان
        if serializer.is_valid():
            serializer.save(
                owner=request.user,
            )

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

def ad_not_found():

    return ({"error": " the Ad not found " },status.HTTP_404_NOT_FOUND),

def ad_not_allowed():
    return ({"error": " not allowed " },status.HTTP_403_FORBIDDEN)


class AdDetail(APIView):

    permission_classes = [IsAuthenticated]

    #  جلب الإعلان باستخدام الـ ID أو الـ PK
    def get_object(self,pk):
        # - التحقق من وجود الإعلان داخل قاعدة البيانات
        try:
            return Ad.objects.get(pk=pk)

        except Ad.DoesNotExist:
            raise Http404

    def get(self, request,pk):
        ad = self.get_object(pk)
        if not ad.is_active:
            return ({"error": " the Ad not found " },status.HTTP_404_NOT_FOUND)
        if ad.owner != request.user:
            ad_not_allowed()

        serializer = AdDetailSerializer(ad)
        return Response(serializer.data)

    def put(self, request,pk):
        ad = self.get_object(pk)

        if not ad.is_active:
            ad_not_found()

        if ad.owner != request.user:
          ad_not_allowed()

        serializer = AdDetailSerializer(ad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):

        ad = self.get_object(pk)
        if not ad.is_active:
            ad_not_found()

        if ad.owner != request.user:
            ad_not_allowed()
        ad.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


# الاعلانات المموله وعرضها
# View مسؤول عن جلب الإعلانات الممولة الشغاله وتحويلها إلى JSON وإرجاعها عبر API.
class Adsponsored(APIView):

    def get(self,request):
        ads = Ad.objects.filter(
            is_active=True,
            ad_status = 'sponsored',
        )
        serializer = AdListSerializer(
            ads,
            many=True,
        )
        return Response(serializer.data)


# ترتيب الاعلانات
#  View مسؤول عن جلب أحدث الإعلانات وترتيبها من الأحدث إلى الأقدم وإرجاعها عبر API.
class Adfeatured(APIView):
    def get_object(self,request):
        ads = (Ad.objects.filter(
            is_active=True,
        )
               .erder_by('-created_at'))

        serializer = AdListSerializer(
            ads,
            many=True,
        )
        return Response(serializer.data)

# عرض عدد مشاهدات الاعلان
class AdPopular(APIView):
    def get(self,request):
        ads = Ad.objects.filter(
            is_active=True,
        ).order_by('-quantity')

        serializer = AdListSerializer(
            ads,
            many=True,
        )
        return Response(serializer.data)












# Create your views here.
