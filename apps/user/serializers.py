from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from rest_framework.authtoken.models import Token


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_active', 'email')
        read_only_fields = ('id', 'is_active', 'is_staff')

        def get_auth_token(self, obj):
            token = Token.objects.create(user=obj)
            return token.key


class EmptySerializer(serializers.Serializer):
    pass


class UserSignupSerializer(serializers.ModelSerializer):
    """
    A user serializer for registering the user
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')

    @staticmethod
    def validate_user(value):
        user = User.objects.filter(username=value)
        if user:
            raise serializers.ValidationError("Username is already taken")
        return value

    @staticmethod
    def validate_password(value):
        password_validation.validate_password(value)
        return value


class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('Current password does not match')
        return value

    def validate_new_password(self, value):
        password_validation.validate_password(value)
        return value
