from django.db import models
from django.utils import timezone
from account.models import User

# Create your models here.

class SetCreditPurchased(models.Model):
    credit_amount = models.PositiveIntegerField(default=0)
    price_amount = models.FloatField()
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(default=timezone.now())


    def __str__(self):
        return f"Credit {self.credit_amount} Price {self.price_amount}"

    class Meta:
        verbose_name_plural = 'Set Purchased Credits'


class CreditPurchasedByUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_purchased_credit", blank=True, null=True)
    credit_amount = models.PositiveIntegerField(default=0)
    credit_price = models.PositiveIntegerField(blank=True, null=True)
    transaction_id = models.CharField(max_length=50,null=True,blank=True)
    payment_id = models.CharField(max_length=50,null=True,blank=True)
    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name_plural = 'Credit Purchased By Users'

    def __str__(self):
        return self.user.full_name

