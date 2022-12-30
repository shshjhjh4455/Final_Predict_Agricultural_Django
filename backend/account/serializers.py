from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            nickname=validated_data["nickname"],
            name=validated_data["name"],
            password=validated_data["password"],
            location=validated_data["location"],
            area=validated_data["area"],
        )
        return user

    class Meta:
        model = User
        fields = ["nickname", "email", "name", "location", "area", "password"]
