from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Orders
from .serializer import OrdersSerializer


class OrdersNormalView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_authenticated:
            orders = Orders.objects.filter(user=request.user)
            serializer = OrdersSerializer(orders,many=True)

            return Response(serializer.data)
        else:
           return Response(
               {"message": "You are not logged in"}, status=status.HTTP_401_UNAUTHORIZED)


    def post(self, request):
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request,pk):
        try:
            orders = Orders.objects.get(user=request.user,id=pk)

        except Orders.DoesNotExist:
            return Response(
                {"message": "Order does not exist"},status=status.HTTP_404_NOT_FOUND)

        serializer = OrdersSerializer(orders, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        try:
            orders = Orders.objects.get(id=pk, user=request.user)

        except Orders.DoesNotExist:
            return Response({"message": "Order does not exist"}, status=status.HTTP_404_NOT_FOUND)

        orders.delete()

        return Response({"message": "Order deleted"}, status=status.HTTP_204_NO_CONTENT)


class OrderListView(APIView):
    permission_classes = (IsAuthenticated,)

    # يجيب كل orders المتكامله وترتيب من الاحداث لي الاقدم
    def get(self,request):
        orders = Orders.objects.filter(user=request.user).order_by('-created_at')

        # يبجيب قيمة orders من urls
        status_param = request.GET.get('status_order')

        #  تصفية orders
        if status_param:
            orders = orders.filter(status=status_param)

        search_param = request.GET.get('search_order')
        if search_param:
            orders = orders.filter(
            # هات الطلبات اللي اسم المنتج or الخدمة الي فيها الكلمة اللي المستخدم كتبها
            (Q(product_name__icontains=search_param) or
             Q(service_name__icontains=search_param))
            )


        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)






# Create your views here.
