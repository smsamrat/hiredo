from .models import *
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User,auth
from rest_framework import exceptions
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.exceptions import ValidationError
from profile_settings.models import *


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    user_profile_pic = serializers.SerializerMethodField()

    def get_user_profile_pic(self, obj):
        try:
            profile = Profile.objects.get(user=obj)
            if profile.image:
                request = self.context.get('request')
                if request is not None:
                    return request.build_absolute_uri(profile.image.url)
                else:
                    return f"{settings.BASE_URL}{profile.image.url}"
        except Profile.DoesNotExist:
            return None


    class Meta:
        model = User
        fields = ['id', 'full_name', 'user_profile_pic', 'email', 'date_of_birth', 'phone_number', 'corporation_name',  'corporation_number', 'is_professional', 'is_user', 'password', 'stripe_customerId']


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResetPasswordOTPSerializer(serializers.Serializer):
    MEDIA_CHOICES = (
        ('phone', 'Phone'),
        ('email', 'Email'),
    )
    media = serializers.ChoiceField(choices=MEDIA_CHOICES)
    phone_or_email = serializers.CharField(required=True)


class VerifyOTPSerializer(serializers.Serializer):
    phone_or_email = serializers.CharField(required=True)
    otp = serializers.CharField(required=True)


class ResetPasswordSerializer(serializers.Serializer):
    phone_or_email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


#service serializers
class ServiceSerializer(serializers.ModelSerializer):
    service_location = serializers.PrimaryKeyRelatedField(
        queryset=ServiceLocation.objects.all(),
        many=True,
    )
    class Meta:
        model = Service
        fields = ['id', 'user', 'service_name', 'service_description','service_location','created_at', 'updated_at']
        depth = 2


class ServiceLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceLocation
        fields = ['id', 'city', 'user', 'distance', 'latitude', 'longitude','created_at', 'updated_at']
        depth=1


class SMSTemplateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = SMSTemplate
        fields = ['id','user','template_name','message', 'created', 'updated']


class EmailTemplateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = EmailTemplate
        fields = ['id','user','template_name','message', 'created_at', 'updated_at']


class OneClickResponseSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.full_name')
    class Meta:
        model = OneClickResponse
        fields = ['id','user','one_click_response','template']
        depth=1


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'image', 'created_at', 'updated_at']
