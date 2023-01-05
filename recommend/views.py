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
from django.db.models import Q


# 사용자로 부터 달과 지역을 입력받아서 예측값을 출력
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

# @login_required(login_url="common:login")
# def predict(request):
#     if request.method == "POST":
#         form = PredictForm(request.POST)
#         if form.is_valid():
#             location = form.cleaned_data.get("location")
#             month = form.cleaned_data.get("month")
#             PredictionInput.objects.create(location=location, month=month)
#             obj = PredictionInput.objects.last()
#             mon2 = obj.month + 1
#             mon3 = obj.month + 2

#             baechoo1 = baechoo_new.objects.get(
#                 (baechoo_new.location == obj.location) & (baechoo_new.month == obj.month)
#             )
#             baechoo2 = baechoo_new.objects.get(
#                 (baechoo_new.location == obj.location) & (baechoo_new.month == mon2)
#             )
#             baechoo3 = baechoo_new.objects.get(
#                 (baechoo_new.location == obj.location) & (baechoo_new.month == mon3)
#             )

#             obj_list = [baechoo1, baechoo2, baechoo3]
#             obj_list = [obj_list]
#             obj_list = np.array(obj_list)
#             obj_list = obj_list.reshape(1, 3, 1)
#             print(obj_list)

#             with open("model/xgb_baechoo_bin_classify_scaler_jinhyeok.pkl", "rb") as s:
#                 scaler = joblib.load(s)
#                 feature = scaler.transform(obj_list)

#             with open("model/xgb_baechoo_bin_classify_jinhyeok.pickle", "rb") as f:
#                 model = pickle.load(f)
#                 y_p = model.predict(feature)

#             if y_p == 1:
#                 y_p = "배추 생산이 가능한 지역으로 예측됩니다."
#             else:
#                 y_p = "배추 생산이 불가능한 지역으로 예측됩니다."

#             user = request.user
#             user_info = UserInfo.objects.get(user=user)

#             context = {
#                 "user_info": user_info,
#                 "form": form,
#                 "y_p": y_p,
#             }
#             return render(request, "common/recommend.html", context)
#     else:
#         form = PredictForm()
#         user = request.user
#         user_info = UserInfo.objects.get(user=user)
#         context = {
#             "user_info": user_info,
#             "form": form,
#             "y_p": None,
#         }
#         return render(request, "common/recommend.html", context)
