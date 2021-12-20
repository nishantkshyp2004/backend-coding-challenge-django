from rest_framework import serializers
from note_taking.models import NoteTaking
from django.contrib.auth.models import User


class NoteTakingSerializer(serializers.ModelSerializer):
    """
    NoteTaking Serializer class.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = NoteTaking
        fields = ['owner', 'title', 'body', 'tags', 'visibility']


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer class.
    """

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
