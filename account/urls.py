from django.urls import path

from .import views

urlpatterns = [
    path('register/' , views.RegisterUser.as_view() ),
    path('change_password/', views.Change_password.as_view() ),

]
