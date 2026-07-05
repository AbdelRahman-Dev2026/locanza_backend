from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category_img/")
    description = models.TextField()

    def __str__(self):
        return self.name


class Serviceprofile(models.Model):

       owner = models.ForeignKey(User, on_delete=models.CASCADE)
       category = models.ForeignKey(Category, on_delete=models.CASCADE)

       business_name = models.CharField(max_length=100)
       image = models.ImageField(upload_to='service_img/')
       location = models.CharField(max_length=100)
       working_hours = models.IntegerField()
       description = models.TextField()

       def __str__(self):
           return self.business_name


class Product(models.Model):

    service = models.ForeignKey(Serviceprofile, on_delete=models.CASCADE, related_name="products")

    name =models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Create your models here.

# **============================**
# **================================**


#  التاني : الخدمات (Services)
# كمستهلك
# أريد تصفح الخدمات حسب القسم والمنطقة
# حتى أصل للخدمة المناسبة بسرعة.
#
# كمستهلك
# أريد البحث عن خدمة أو محل
# حتى أتمكن من العثور على ما أحتاجه بسهولة.
#
# كصاحب خدمة
# أريد إضافة منتجات أو خدمات داخل صفحتي
# حتى يستطيع العملاء طلبها.
#
