from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from .Serializer import UserSerializer, ChangePasswordSerializer,LoginSerializer

from rest_framework import permissions

from django.contrib.auth.hashers import check_password

from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework_simplejwt.exceptions import TokenError



from django.contrib.auth import get_user_model
User = get_user_model()




class loginAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)


        if  check_password(password, user.password):
            return Response({"message", "login successfully"}, status=status.HTTP_200_OK)


        Token = RefreshToken.for_user(user)
        return Response({"refresh": str(Token), "access": str(Token.access_token),

            "user": {
                "id": user.id,
                "email": user.email,
                'role': user.role,
            }
        })


class RefreshTokenAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        try:
            Token = request.data.get('token')

            refresh = RefreshToken(Token)

            access_token = str(refresh.access_token)

            return Response({"access": (access_token),})

        except TokenError:
            return Response({"error": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        try:
            token = request.data.get('token')
            refresh = RefreshToken(token)
            refresh.blacklist()
            return Response({"message": "Logged out successfully",}, status=status.HTTP_200_OK)

        except Exception:
            return Response({"error": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)


class RegisterUser(APIView):
     permission_classes = [permissions.AllowAny]

     def post(self, request,):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


     def get(self, request, pk=None):

        if pk is None:  #  مفيش pk رجع كل users
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data)

        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user).data
            return Response(serializer, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response(
                {'Error': "user not found",},status=status.HTTP_404_NOT_FOUND
            )


     def put(self, request, pk):

        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


     def delete(self, request, pk):
        user = User.objects.get(id=pk)
        if request.user != user:
            return Response(status=status.HTTP_403_FORBIDDEN_NO_CONTENT )

        user.delete()
        return Response(
            {"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT
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
                  {"error": "Old password is incorrect"},status=status.HTTP_400_BAD_REQUEST
                )

            user.set_password(new_password)
            user.save()

            return Response(
              {"message": "Password changed successfully"}, status=status.HTTP_200_OK
              )

        return Response(
            {"error": "Password not changed"}, status=status.HTTP_400_BAD_REQUEST
        )




# Create your views here.

# =======================
# =========================

# **** المطلوب ***
# 1. get = عرض البيانات
# 2. update = تعديل بيانات المستخدم
# 3. change_password  = تغيير
# 4.register_user= إنشاء حساب جديد


