from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    area = forms.CharField(label="지역")
    location = forms.CharField(label="위치")
    phone = forms.CharField(label="전화번호")

    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
            "email",
            "area",
            "location",
            "phone",
        )
