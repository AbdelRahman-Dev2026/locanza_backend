from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Payment,PaymentStatus
from .serializer import PaymentSerializer



class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        payments = Payment.objects.filter(user=request.user)
        serializer = PaymentSerializer(payments, many=True)

        return Response(
            serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user,)

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class PaymentDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self,request,pk):
        try:
            payment = Payment.objects.get(user=request.user, pk=pk)

        except Payment.DoesNotExist:
            return Response({"message": "Payment not found"},status=status.HTTP_404_NOT_FOUND)

        serializer = PaymentSerializer(payment,data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user,)

            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(
            serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        try:
            payment=Payment.objects.get(user=request.user,pk=pk)

        except Payment.DoesNotExist:
            return Response(
                {"message": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)

        payment.status = PaymentStatus.CANCEL
        payment.save()
        return Response(
            {"message": "Payment Successfully cancelled"},status=status.HTTP_200_OK)














# Create your views here.
