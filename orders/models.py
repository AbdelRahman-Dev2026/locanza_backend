from django.db import models

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from services.models import Serviceprofile,Product

User = get_user_model()

# حالات الطلب
class OrderStatus(models.TextChoices):

    PENDING = ('pending', 'Pending')  # الطلب اتعمل ولسه ما اتقبلش
    ACCEPTED = ('accepted', 'Accepted')  # اتوافق عليه
    PREPARING = ('preparing', 'Preparing')  # بيتجهز
    ON_DELIVERY = ('on_delivery', 'On_Delivery') # في الطريق
    COMPLETED = ('completed', 'Completed')  # اتسلم
    CANCELLED = ('cancelled', 'Cancelled')  # اتلغي


class Orders(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    service = models.ForeignKey(Serviceprofile, on_delete=models.CASCADE, related_name='orders')

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    status = models.CharField(max_length=20, choices=OrderStatus, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f"order {self.product}")











# Order = عملية الشراء نفسها
# يعني:
# مين اشترى
# اشترى إيه
# حالة الطلب إيه





# Create your models here.






# **============================**
# **================================**
# سادسًا: الطلبات (Orders)
# كمستهلك
# أريد إنشاء طلب من أي خدمة
# حتى أستطيع شراء المنتجات بسهولة.
#
# كصاحب خدمة
# أريد استقبال الطلبات وإدارتها
# حتى أتمكن من متابعة العملاء وتنفيذ الطلبات.
#===============================================
