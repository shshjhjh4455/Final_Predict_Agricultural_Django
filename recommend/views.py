from django.shortcuts import render
from django.http import HttpResponse
import pickle
import joblib
from common.models import UserInfo
from django.contrib.auth.decorators import login_required


def predict(request):
    example = [
        [
            22.30,
            31.20,
            14.50,
            233.70,
            339.280,
            17.10,
            28.50,
            4.40,
            177.10,
            250.480,
            9.30,
            20.60,
            -1.80,
            77.50,
            246.490,
        ]
    ]
    with open("model/xgb_baechoo_bin_classify_scaler_jinhyeok.pkl", "rb") as s:
        scaler = joblib.load(s)
        feature = scaler.transform(example)

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
        return render(request, "common/recommend.html", {"y_p": "배추 농사 재배가 불가능합니다."})
