from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    phone = forms.CharField(label="전화번호")
    area = forms.CharField(label="면적")
    location = forms.CharField(label="위치")

    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
            "email",
            "phone",
            "area",
            "location",
        )
