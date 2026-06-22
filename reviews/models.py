from django.db import models

from django.contrib.auth import get_user_model

from services.models import Serviceprofile

from django.core.validators import MinValueValidator, MaxValueValidator


user= get_user_model()

class Review(models.Model):

    user = models.ForeignKey(user,on_delete=models.CASCADE)

    service = models.ForeignKey(
        Serviceprofile,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    rating = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    likes_count = models.IntegerField(default=0)
    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)






# Create your models here.


## **============================**
# **================================**
# رابعا: التقييمات والتعليقات
# كمستهلك
# أريد تقييم الخدمة وكتابة تعليق
# حتى أشارك تجربتي مع الآخرين.
#
# كصاحب خدمة
# أريد رؤية تقييمات العملاء
# حتى أتمكن من تحسين الخدمة.

