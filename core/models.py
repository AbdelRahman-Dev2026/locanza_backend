from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# دي خاصة بصور الاعلانات وافضل الخدمات والعرض
class Banner(models.Model):

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banner/%Y/%m')
    link = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# دي خاصة بي الصور المتحركة
class Slider(models.Model):

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='slider/%Y/%m')
    # ترتيب رقم Sliders
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# اقسام الصفحة الرئيسية
class HomeCategory(models.Model):
    title = models.CharField(max_length=200)
    # تظيم شكل واسم urls
    slug = models.SlugField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title







# Create your models here.


# **=====================**
# 1.Home.
# 2.about.
# 3.contact
# **===========================**

# ثامنا: الصفحة الرئيسية (Home)
# كمستخدم مستهلك
# أريد رؤية:
# بوستات الخدمات التي أتابعها
# أحدث العروض والإعلانات
# الخدمات القريبة مني
# الخدمات المميزة (Sponsored)
# حتى أستطيع معرفة أحدث العروض والخدمات في منطقتي بسهولة.
