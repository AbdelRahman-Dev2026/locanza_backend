from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category,Serviceprofile,Product

from rest_framework.permissions import (
AllowAny,
IsAuthenticated,
IsAdminUser,
)

from .permissions import IsOwnerOrAdmin, IsProductOwnerOrAdmin
from .serializer import(
    CategorySerializer,
    ServiceProfileSerializer,
    ProductSerializer
    )

# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]


class ServiceProfileViewSet(ModelViewSet):
    queryset = Serviceprofile.objects.all()
    serializer_class = ServiceProfileSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        if self.action in ['create']:
            return [IsAuthenticated()]

        return [IsOwnerOrAdmin()]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # الصلاحيات تتغير حسب العملية الحالية
    def get_permissions(self):
        # أي شخص يقدر يشوف المنتجات
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        # لازم يكون عامل login عشان يضيف منتج
        if self.action in ['create']:
            return [IsAuthenticated()]
        return [IsProductOwnerOrAdmin()]









#
# #
# إذًا في مشروعك غالبًا
# Category
# Read فقط للمستخدمين.
# Create/Update/Delete للأدمن.
# ServiceProfile
# صاحب الخدمة ينشئ ويعدل ويحذف نشاطاته.
# Product
# صاحب الخدمة ينشئ ويعدل ويحذف منتجات نشاطاته.
#
# وده يعتبر الحد الأدنى المطلوب من الـ Views في App service.


# get_permissions() تحدد أي صلاحيات سيتم استخدامها لهذا الطلب الحالي.باي طريقة اي بي الطريقة المناسبة