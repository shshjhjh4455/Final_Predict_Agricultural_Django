from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            nickname=validated_data["nickname"],
            name=validated_data["name"],
            location=validated_data["location"],
            area=validated_data["area"],
            phone=validated_data["phone"],
            password=validated_data["password"],
        )
        return user

    # @property
    # def is_staff(self):
    #     return self.is_admin

    class Meta:
        model = User
        fields = [
            "id",
            "nickname",
            "email",
            "name",
            "location",
            "area",
            "phone",
            "password",
        ]
