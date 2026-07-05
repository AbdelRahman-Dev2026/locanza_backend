from django.urls import path

from .views import *


urlpatterns = [
    path('login/', loginAPIView.as_view()),

    path('token/refresh/', RefreshTokenAPIView.as_view(), name='RefreshToken'),
    path('logout/', LogoutAPIView.as_view(), name='Logout'),

    path('register/', RegisterUser.as_view() ),
    path('change_password/', Change_password.as_view() ),

]
