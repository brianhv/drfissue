from rest_framework import viewsets
from drftest.readonly import serializers
from drftest.readonly.models import ContactInfo

class UserViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = serializers.ProfileSerializer

