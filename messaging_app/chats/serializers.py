from rest_framework import serializers
from .models import User, Message, Conversation
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'user_id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'role',
            'created_at'
        ]
        read_only_fields = ['created_at, user_id, password_hash']

    def create(self, validated_data):
        validated_data['password_hash'] = make_password(
            validated_data['password'])
        return super().create(validated_data)


def MessageSerializer(serializers)
