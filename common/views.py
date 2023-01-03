from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from common.models import UserInfo
=======
from common.forms import UserForm
>>>>>>> parent of 591a96a9 (make user info)


def signup(request):
    if request.method == "POST":
<<<<<<< HEAD
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        area = request.POST["area"]
        location = request.POST["location"]
        phone = request.POST["phone"]
        user = User.objects.create_user(
            username=username, password=password, email=email
        )
        user_info = UserInfo(user=user, area=area, location=location, phone=phone)
        user_info.save()
        return redirect("common:login")
=======
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
>>>>>>> parent of 591a96a9 (make user info)
    else:
        return render(request, "common/signup.html")


def mypage(request):
    user_info = UserInfo.objects.get(user=request.user)
    return render(request, "common/mypage.html", {"user_info": user_info})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("pybo:index")
        else:
            return render(
                request, "common/login.html", {"error": "아이디 또는 비밀번호가 잘못되었습니다."}
            )
    else:
        return render(request, "common/login.html")


def logout(request):
    auth_logout(request)
    return redirect("pybo:index")
