from rest_framework import serializers
from .models import *

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        
class InboxSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='user.full_name')
    class Meta:
        model = Message
        fields = ['user','full_name']
