from rest_framework import serializers
from django.contrib.auth.models import Group, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class AuthStatusSerializer(serializers.Serializer):
    status = serializers.CharField()
