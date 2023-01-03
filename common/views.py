from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            location = form.cleaned_data.get("location")
            area = form.cleaned_data.get("area")
            phone = form.cleaned_data.get("phone")
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(
                username=username,
                password=raw_password,
                location=location,
                area=area,
                email=email,
                phone=phone,
            )  # 사용자 인증
            login(request, user)  # 로그인
            return redirect("index")
    else:
        form = UserForm()
    return render(request, "common/signup.html", {"form": form})


def mypage(request):
    return render(request, "common/mypage.html")
