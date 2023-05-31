from rest_framework import serializers
from profile_settings.models import *
from profile_settings import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf import settings
from account.serializers import *

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = [ 'id','user','title', 'description','image', 'long_description']


class AboutSerializer(serializers.ModelSerializer):
    company_logo = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    profile_image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    class Meta:
        model = About
        fields = [
        'user',
        'company_name',
        'company_logo',
        'profile_image',
        'email',
        'phone',
        'websit_link',
        'location',
        'company_siz',
        'years_of_business',
        'discription',
        'created_at',
        'updated_at',
        ]


class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    class Meta:
        model = Photo
        fields = [
            'id',
        'user',
        'image',
        'created_at'
        ]

class SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_Media_Link
        fields = [
        'user',
        'facebook',
        'twitter',
        'instagram',
        'linkdin',
        'websit_link',
        ]


class Account_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account_Details
        fields = [
        'user',
        'account_email',
        'usage_contact',
        'sms_notification_number',

        ]

class ReviewRatingSerializer(serializers.ModelSerializer):
    reviewed_by = RegistrationSerializer(required=False)
    class Meta:
        model = ReviewRating
        fields = [
            'id',
            'reviewed_by',
            'reviewed_user',
            'rating',
            'comment',
            'created'
        ]

        # depth=2



#work by swesadiqul
class ProfileSerializer(serializers.ModelSerializer):
    percentage_complete = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    def get_percentage_complete(self, obj):
        return obj.percentage_complete()

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            if request is not None:
                return request.build_absolute_uri(image_url)
            else:
                return f"{settings.BASE_URL}{image_url}"
        else:
            return None

    class Meta:
        model = Profile
        fields = ('id', 'user', 'image', 'credit', 'badges', 'updated_at', 'percentage_complete')
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    reviews_received = ReviewRatingSerializer(many=True)
    user_profile_pic = serializers.SerializerMethodField()

    def get_user_profile_pic(self, obj):
        try:
            profile = obj.user_profile
            serializer = ProfileSerializer(profile, context=self.context)
            return serializer.data.get('image')
        except Profile.DoesNotExist:
            return None

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'user_profile_pic', 'date_of_birth', 'phone_number',
            'corporation_name', 'corporation_number', 'is_professional', 'is_user', 'reviews_received']
        depth = 1


class HelpTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpTopic
        fields = ('id', 'title')


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ('id', 'topic', 'question', 'answer')
        # depth = 1


class StillNeedHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = StillNeedHelp
        fields = ('id', 'email', 'message')




