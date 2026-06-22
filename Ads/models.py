from django.db import models

from django.contrib.auth import get_user_model
from services.models import Serviceprofile,Product

User = get_user_model()


class Ad(models.Model):

    #    نوع الاعلانات
    AD_TYPES=(
    ('normal', 'Normal'),
    ('sponsored', 'Sponsored'),
    )

    # حاله الدفع فى الاعلان
    PAYMENT_TYPES=(
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('failed', 'Failed'),
    )

    # علاقات الربط
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    service = models.ForeignKey(Serviceprofile, on_delete=models.CASCADE, null=True, blank=True,)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True,)

    title = models.CharField(max_length=150)
    image = models.ImageField()
    description = models.TextField()
    link = models.URLField(null=True, blank=True)

    ad_status = models.CharField(max_length=10, choices=AD_TYPES, default='normal')
    payment_status = models.CharField(max_length=10, choices=PAYMENT_TYPES, default='pending')

    price = models.DecimalField(max_digits=10, decimal_places=2 ,default=0)
    quantity = models.PositiveIntegerField(default=0)


    # هل الإعلان شغال أو لا؟
    is_active = models.BooleanField(default=True)
    # يتسجل الوقت مرة واحدة فقط عند إنشاء السجل
    created_at = models.DateTimeField(auto_now_add=True)
    # يتحدث تلقائيًا كل مرة يتم تعديل السجل
    updated_at = models.DateTimeField(auto_now=True)

    started_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)




# Create your models here.



## **============================**
# **================================**
# التالت: الإعلانات (Ads)
# كصاحب خدمة
# أريد عمل إعلان ممول لخدمتي أو منتج معين
# حتى يظهر لعدد أكبر من المستخدمين داخل المنطقة.
#
# كمستخدم
# أريد رؤية الإعلانات المناسبة لمنطقتي واهتماماتي
# حتى أستفيد من العروض القريبة مني.

