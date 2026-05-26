from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from .Serializer import UserSerializer, ChangePasswordSerializer
from rest_framework import status, permissions

from .models import User


# Create your views here.


class RegisterUser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        permission_classes = [permissions.AllowAny]

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def get(self, requset, pk=None):


        if pk is None:  # ول مفيش pk رجع كل users
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data)
        # دا لو فى user رجع user دا فقط
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user).data
            return Response(serializer, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response(
                {'Error': "user not found",},
                status=status.HTTP_404_NOT_FOUND
            )

    # تعديل  users
    def put(self, request, pk):

        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        user = User.objcets.get(id=pk)
        user.delete()
        return Response(
            {"message": "Deleted successfully"},
                        status=status.HTTP_204_NO_CONTENT
        )


class Change_password(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        serializer = ChangePasswordSerializer()
        return Response(serializer.data)


    def put(self, request):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():

            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']

            user = request.user

            if not user.check_password(old_password):
                return Response(
                  {"error": "Old password is incorrect"},
                   status=status.HTTP_400_BAD_REQUEST
                )

            user.set_password(new_password)
            user.save()

            return Response(
              {"message": "Password changed successfully"},
               status=status.HTTP_200_OK
              )

        return Response(
            {"error": "Password not changed"},
            status=status.HTTP_400_BAD_REQUEST
        )





# =======================
# =========================

# **** المطلوب ***
# 1. get = عرض البيانات
# 2. update = تعديل بيانات المستخدم
# 3. change_password  = تغيير
# 4.register_user= إنشاء حساب جديد


