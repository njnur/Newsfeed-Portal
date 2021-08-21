from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User


def get_and_authenticated_user(username, password):
    user = authenticate(username=username, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return user


def create_user_account(email, password, username, **extra_fields):
    user = User.objects.create_user(
        username=username, email=email, password=password, **extra_fields)
    return user
