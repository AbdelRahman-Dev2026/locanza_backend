from django.shortcuts import render

from rest_framework.response import Response

from . import serializer

from rest_framework.views import APIView

from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import ReviewsSerializer

from .models import Review


class ReviewsView(APIView):

    def get_permissions(self):
        if self.request.method == 'Get':
            return [AllowAny(),]
        else:
            return [IsAuthenticated(),]

    def get(self,request):
        review = Review.objects.all()

        serializer = ReviewsSerializer(
            review,
            many=True
        )

        return Response(serializer.data)


    def post(self,request):

        serializer = ReviewsSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            serializer.save(
                user=request.user,
            )
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    def put(self,request,pk):

        review = Review.objects.get(id=pk)
        serializer = ReviewsSerializer(
            review,
            data=request.data,
        )

        if serializer.is_valid():
            serializer.save(
                user=request.user,
            )
            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    def delete(self,request,pk):
        try:
            review = Review.objects.get(id=pk)
        except Review.DoesNotExist:
            return Response({"Error": "not found"},status=status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


























# Create your views here.
