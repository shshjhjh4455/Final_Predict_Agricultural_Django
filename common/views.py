from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from common.models import UserInfo
from common.forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


# signup에서 사용자로 부터 면적, 위치, 전화번호를 받아옴
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone = form.cleaned_data.get("phone")
            area = form.cleaned_data.get("area")
            location = form.cleaned_data.get("location")
            # NOT NULL constraint failed common_userinfo.user_id
            UserInfo.objects.create(
                user=user, phone=phone, area=area, location=location
            )
            auth_login(request, user)
            return redirect("furoot:index")
    else:
        form = UserForm()
    return render(request, "common/signup.html", {"form": form})


# 로그인
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("furoot:index")
    else:
        form = AuthenticationForm()
    return render(request, "common/login.html", {"form": form})


# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect("furoot:index")


# 마이페이지에서는 로그인한 사용자의 정보와 common uer_info df를 보여줌
@login_required(login_url="common:login")
def mypage(request):
    user = request.user
    user_info = UserInfo.objects.get(user=user)
    return render(request, "common/mypage.html", {"user_info": user_info})


# 회원탈퇴
