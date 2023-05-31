from .models import *
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User,auth
from rest_framework import exceptions
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.exceptions import ValidationError




class SetCreditPurchasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetCreditPurchased
        fields = '__all__'


class CreditPurchasedByUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditPurchasedByUser
        fields = '__all__'
        
class CurrentUserCreditAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditPurchasedByUser
        fields = ('credit_amount',)