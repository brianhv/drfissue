from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from drftest.readonly.models import ContactInfo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    class Meta:
        model = ContactInfo
        fields = ('city', 'first_name', 'last_name', 'url')
