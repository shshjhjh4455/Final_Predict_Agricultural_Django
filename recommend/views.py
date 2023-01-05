from django.shortcuts import render
from django.http import HttpResponse
import pickle
import joblib
from common.models import UserInfo
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import PredictionInput
from .forms import PredictForm
from save_csv.models import baechoo_new
from rest_framework import viewsets
import pickle
import numpy as np
from django.views.decorators.http import require_POST


@login_required
def predict(request):

    if request.method == "POST":
        form = PredictForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data.get("location")
            month = form.cleaned_data.get("month")
            PredictionInput.objects.create(location=location, month=month)
            obj = PredictionInput.objects.last()
            mon2 = obj.month + 1
            mon3 = obj.month + 2
            
            baechoo1 = baechoo_new.objects.get(
                (baechoo_new.location == obj.location)
                & (baechoo_new.month == obj.month)
            )
            baechoo2 = baechoo_new.objects.get(
                (baechoo_new.location == obj.location) & (baechoo_new.month == mon2)
            )
            baechoo3 = baechoo_new.objects.get(
                (baechoo_new.location == obj.location) & (baechoo_new.month == mon3)
            )

            obj_list = [baechoo1, baechoo2, baechoo3]
            input_list = []
            for i in range(len(obj_list)):
                input_list.append(obj_list[i].avr)
                input_list.append(obj_list[i].max)
                input_list.append(obj_list[i].min)
                input_list.append(obj_list[i].rain)
                input_list.append(obj_list[i].sun)

        # example = [
        #     [
        #         22.30,
        #         31.20,
        #         14.50,
        #         233.70,
        #         339.280,
        #         17.10,
        #         28.50,
        #         4.40,
        #         177.10,
        #         250.480,
        #         9.30,
        #         20.60,
        #         -1.80,
        #         77.50,
        #         246.490,
        #     ]
        # ]
        with open("model/xgb_baechoo_bin_classify_scaler_jinhyeok.pkl", "rb") as s:
            scaler = joblib.load(s)
            pred_test = np.array(input_list).reshape(1, -1)
            feature = scaler.transform(pred_test)

        with open("model/xgb_baechoo_bin_classify_jinhyeok.pickle", "rb") as f:
            model = pickle.load(f)
            y_p = model.predict(feature)

        user = request.user
        user_info = UserInfo.objects.get(user=user)

        if y_p == 1:
            # y_p, user_info를 recommend.html에 넘겨줌
            return render(
                request,
                "common/recommend.html",
                {"y_p": "배추 농사 재배가 가능합니다.", "user_info": user_info},
            )
        else:
            return render(
                request, "common/recommend.html", {"y_p": "배추 농사 재배가 불가능합니다."}
            )
