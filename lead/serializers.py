from rest_framework import serializers
from .models import *
# from django.contrib.auth import get_user_model
from account.models import *
# User = get_user_model()
from account.serializers import *
from profile_settings.serializers import *
from rest_framework.decorators import action

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id','question','options','credit']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['question'] = {"qs":instance.question.qs}
        return data


class QuestionsSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True,required=False)
    class Meta:
        model = Questions
        fields = ['id','qs','answers','cat',]
        depth = 1
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['cat'] = {"name":instance.cat.name,}
    #     return data

class CategorySerializer(serializers.ModelSerializer):
    cat_name = QuestionsSerializer(many=True,required=False)
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    class Meta:
        model = Category
        fields = ['id','name','image','cat_name','children','popularity']
        depth = 1

    def get_fields(self):
        fields = super().get_fields()
        fields['children'] = CategorySerializer(many=True, read_only=True)
        return fields


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['category','question','location','p_answer']
        depth = 1

class PostListSerializer(serializers.ModelSerializer):
    # post_object = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), many=True)
    user = RegistrationSerializer()
    class Meta:
        model = PostList
        fields = ('id','user','location','latitude','longitude','category','post_object','response_count','post_credit','created',)

        depth = 2

class RecieverEmailTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecieverEmailTemplate
        fields = '__all__'
        # depth = 1

class RealTimeServiceserializer(serializers.ModelSerializer):
    user = UserSerializer()
    service_name = CategorySerializer(required=False)
    total = serializers.FloatField(required=False)
    class Meta:
        model = Service
        fields =['id','user','service_name','service_description','service_location','total']
        depth = 1

class WishlistCompanySerializer(serializers.ModelSerializer):
    wished_user = RegistrationSerializer(required=True)
    product_rating_avg = serializers.ReadOnlyField(read_only=True)
    class Meta:
        model = WishlistProfileService
        fields =['id','user','wished_user','product_rating_avg']
        depth=1

class WishlistFeatureSerializer(serializers.ModelSerializer):
    category_service = CategorySerializer(required=True)
    class Meta:
        model = WishlistFeatureService
        fields =['id','user','category_service',]



#added by swesadiqul
# class PostRequestListSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer(source='user.profile')
#     class Meta:
#         model = PostRequestList
#         fields = ['id', 'post', 'profile', 'rating', 'request_accepted']
#         depth = 1


class PostRequestListSerializer(serializers.ModelSerializer):
    profile_name = serializers.CharField(source='profile.user.full_name')
    userId = serializers.CharField(source='profile.user.id')
    post = PostListSerializer()

    class Meta:
        model = PostRequestList
        fields = ['id', 'post', 'profile_name', 'userId', 'profile', 'rating', 'request_accepted']
        depth = 1


class AcceptRejectSerializer(serializers.Serializer):
    postId = serializers.IntegerField(required=True)
    response = serializers.BooleanField(required=True)
    userId = serializers.IntegerField(required=True)


class MyResponseSerializer(serializers.ModelSerializer):
    posts = PostListSerializer()
    class Meta:
        model = MyResponse
        fields = ['id', 'user', 'posts', 'status', 'created_at']
        depth = 1

class RealTimeBookNowServiceSerializer(serializers.ModelSerializer):
    # posts = PostListSerializer()
    class Meta:
        model = RealTimeBookNowService
        fields = ['question','p_answer']
        # depth = 1

class RealTimeBookNowSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    booked_in_user = UserSerializer()
    booked_user_avg_rating = serializers.FloatField(required=False)
    class Meta:
        model = RealTimeBookNow
        fields = ['id','user','booked_in_user','location','latitude','longitude','category','realtime_post_object','post_credit','post_type','response_count','is_response','booked_user_avg_rating','created']
        depth = 2

class CreditReduceTransactionSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.full_name')
    user_id = serializers.CharField(source='user.id')
    class Meta:
        model = CreditReduceTransaction
        fields = ['id','user_id','user_name','lead_post_id','lead_post_credit','date']


