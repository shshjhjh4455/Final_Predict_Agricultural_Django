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


# 사용자로 부터 달과 지역을 입력받는다
@login_required
def predict(request):
    if request.method == "POST":
        form = PredictForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data["location"]
            month = form.cleaned_data["month"]
            # 사용자가 입력한 값을 DB에 저장한다
            user = UserInfo.objects.get(user=request.user)
            user.location = location
            user.month = month
            user.save()

            # baechoo_new db에서 사용자가 입력한 지역과 월,해당하는 데이터를 가져온다
            baechoo = baechoo_new.objects.filter(location=location, month=month)
            # baechoo_new db에서 사용자가 입력한 지역과 한달 후 월,해당하는 데이터를 가져온다
            baechoo_next = baechoo_new.objects.filter(location=location, month=month + 1)
            # baechoo_new db에서 사용자가 입력한 지역과 두달 후 월,해당하는 데이터를 가져온다
            baechoo_next2 = baechoo_new.objects.filter(location=location, month=month + 2)

            # baechoo, baechoo_next, baechoo_next2 db에서 가져온 데이터를 합친다
            baechoo = baechoo | baechoo_next | baechoo_next2

            # baechoo_new db에서 가져온 데이터를 리스트로 변환한다
            baechoo_list = list(baechoo.values_list())
            # baechoo_new db에서 가져온 데이터를 numpy array로 변환한다
            baechoo_array = np.array(baechoo_list)
            # baechoo_new db에서 가져온 데이터를 2차원으로 변환한다
            baechoo_2d = baechoo_array.reshape(1, -1)

            with open("model/xgb_baechoo_bin_classify_scaler_jinhyeok.pkl", "rb") as s:
                scaler = joblib.load(s)
                feature = scaler.transform(baechoo_2d)

            with open("model/xgb_baechoo_bin_classify_jinhyeok.pickle", "rb") as f:
                model = pickle.load(f)
                y_p = model.predict(feature)

            if y_p == 0:
                result = "배추를 생산하기에 적합하지 않습니다."
            elif y_p == 1:
                result = "배추를 생산하기에 적합합니다."
            else :
                result = "오류"

            return render(request, "common/recommend.html", {"result": result})
    else:
        form = PredictForm(request.POST)
        if form.is_valid():
            location = form.cleaned_data["location"]
            month = form.cleaned_data["month"]
            # 사용자가 입력한 값을 DB에 저장한다
            user = UserInfo.objects.get(user=request.user)
            user.location = location
            user.month = month
            user.save()

            # baechoo_new db에서 사용자가 입력한 지역과 월,해당하는 데이터를 가져온다
            baechoo = baechoo_new.objects.filter(location=location, month=month)
            # baechoo_new db에서 사용자가 입력한 지역과 한달 후 월,해당하는 데이터를 가져온다
            baechoo_next = baechoo_new.objects.filter(location=location, month=month + 1)
            # baechoo_new db에서 사용자가 입력한 지역과 두달 후 월,해당하는 데이터를 가져온다
            baechoo_next2 = baechoo_new.objects.filter(location=location, month=month + 2)

            # baechoo, baechoo_next, baechoo_next2 db에서 가져온 데이터를 합친다
            baechoo = baechoo | baechoo_next | baechoo_next2

            # baechoo_new db에서 가져온 데이터를 리스트로 변환한다
            baechoo_list = list(baechoo.values_list())
            # baechoo_new db에서 가져온 데이터를 numpy array로 변환한다
            baechoo_array = np.array(baechoo_list)
            # baechoo_new db에서 가져온 데이터를 2차원으로 변환한다
            baechoo_2d = baechoo_array.reshape(1, -1)

            with open("model/xgb_baechoo_bin_classify_scaler_jinhyeok.pkl", "rb") as s:
                scaler = joblib.load(s)
                feature = scaler.transform(baechoo_2d)

            with open("model/xgb_baechoo_bin_classify_jinhyeok.pickle", "rb") as f:
                model = pickle.load(f)
                y_p = model.predict(feature)

            if y_p == 0:
                result = "배추를 생산하기에 적합하지 않습니다."
            elif y_p == 1:
                result = "배추를 생산하기에 적합합니다."
            else :
                result = "오류"
        return render(request, "common/recommend.html", {"form": form})





            