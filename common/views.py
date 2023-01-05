from django.shortcuts import render
import pickle
import joblib
from common.models import UserInfo
from django.contrib.auth.decorators import login_required
from .models import PredictionInput
from .forms import PredictForm
from save_csv.models import baechoo_new
import pickle
import numpy as np


# 사용자로 부터 달과 지역을 입력받아서 예측값을 출력
@login_required(login_url="common:login")
def predict(request):
    if request.method == "POST":
        form = PredictForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data.get("location")
            month = form.cleaned_data.get("month")
            PredictionInput.objects.create(location=location, month=month)
            obj = PredictionInput.objects.last()
        
            bae_test= baechoo_new.objects.get(location= obj.location, month=obj.month)

            user = request.user
            user_info = UserInfo.objects.get(user=user)

            context= {
                "user_info":user_info,
                "form":form,
                "obj_test": bae_test.avr,
            }
            return render(request, "common/recommend.html", context)
    else:
        form = PredictForm()
        user = request.user
        user_info = UserInfo.objects.get(user=user)
        context = {
            "user_info": user_info,
            "form": form,
            "y_p": None,
        }
        return render(request, "common/recommend.html", context)