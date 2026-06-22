from django.db import models


from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth import get_user_model

from orders.models import Orders


User = get_user_model()


# =========================
# حالات الدفع او حاله الدفع
# =========================
class PaymentStatus(models.TextChoices):

    PENDING = ('pending', 'Pending')
    PAID = ('paid', 'Paid')
    FAILED = ('failed', 'Failed')
    REFUNDED = ('refunded', 'Refunded')
    CANCEL = ('cancel', 'Cancel')


# =========================
# طرق الدفع
# =========================
class PaymentMethod(models.TextChoices):

    CASH = ('cash', 'Cash')
    CARD = ('card', 'Card')
    WALLET = ('wallet', 'Wallet')
    ONLINE = ('online', 'Online')



class Payment(models.Model):

    user = models.ForeignKey(
        User,on_delete=models.CASCADE, related_name='payments')

    # الطلب المرتبط بالدفع
    order = models.ForeignKey(
        Orders,on_delete=models.CASCADE,related_name='payments')

    # قيم الدفع او قيمة الدفع
    amount = models.DecimalField(
        max_digits=10,  decimal_places=2 )

    #  طرق او طريقة الدفع
    method = models.CharField(
        max_length=20, choices=PaymentMethod.choices, default=PaymentMethod.CASH)

    # حالة الدفع
    status = models.CharField(
        max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.PENDING )

    # رقم العملية المالية
    transaction_id = models.CharField(
        max_length=255,blank=True,null=True
    )

    # وقت الإنشاء
    created_at = models.DateTimeField(auto_now_add=True )

    # وقت التعديل
    updated_at = models.DateTimeField( auto_now=True)



    def __str__(self):
        return f"{self.user} - {self.status}"


















# Create your models here.


# **====================**
# **==========================**

# سابعًا: الدفع (Payment)
# كمستهلك
# أريد الدفع باستخدام وسائل دفع متعددة
# حتى أتمكن من إتمام الطلب بسهولة.
# مثل:
# كاش
# فودافون كاش
# بطاقة بنكية
