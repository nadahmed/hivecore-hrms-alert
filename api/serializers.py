from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from api.models import Notification
from django.contrib.auth import get_user_model

User = get_user_model()

class NotificationSerializer(ModelSerializer):
    username = serializers.CharField(write_only=True)


    class Meta:
        model = Notification
        exclude= ('user', )
 
    def create(self, validated_data):
        username = validated_data.pop('username')
        user, created = User.objects.get_or_create(username=username)
        instance = Notification.objects.create(**validated_data, user=user)
        return instance
    
    def patch(self, instance, validated_data):
        instance.is_read = validated_data['is_read']
        instance.save()
        return instance