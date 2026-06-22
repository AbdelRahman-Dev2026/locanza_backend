from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# user التعديل فى تسجيل المستخدم
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields ):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password , **extra_fields ):

        extra_fields.setdefault('is_staff', True) # هل الحقل دا موجود وله
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)  # هل الحساب “مفعل وشغال” ولا “مقفول”ده يحدد
        return self.create_user(email, password, **extra_fields)

# user العادي
class User(AbstractUser):

    username = None   # ودا معانه أنا مش عاوز username نهائي"

    email = models.EmailField(unique=True)  # كل مستخدم لازم يكون عنده email مختلف

    USERNAME_FIELD = 'email'# إيه الحقل الأساسي اللي المستخدم هيسجل بيه الدخول؟

    # يعني مفيش حقول إضافية إجبارية وقت إنشاء user
    # "إيه الحقول الإضافية المطلوبة وقت إنشاء superuser
    REQUIRED_FIELDS =['phone_number']

    objects = CustomUserManager()
    # دي بتحدد أنواع المستخدمين
    Role_CHOICES = (
        ("user", "User"),
        ("service_provider", "Service_provider"),
    )

    phone_number = models.CharField(max_length = 100)
    role = models.CharField(
        max_length = 100,
        choices = Role_CHOICES,
        default = "user",
    #     ودا كل user لازم يكون نوع معين من اللي انا عاملهم
    )





class location(models.Model):
    pass


# Create your models here.


# **============================**
# **================================**
#الاول: الحسابات (Accounts)
# كمستخدم جديد
# أريد إنشاء حساب بسهولة باستخدام:
# رقم الهاتف
# أو
# البريد الإلكتروني
# حتى أتمكن من استخدام التطبيق.
#
# كصاحب خدمة
# أريد إنشاء صفحة خاصة بخدمتي تحتوي على:
# اسم النشاط
# الصور
# الموقع
# أوقات العمل
# وصف الخدمة
# حتى يتمكن العملاء من الوصول إليّ.






