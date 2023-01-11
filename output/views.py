from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from common.models import UserInfo
from .models import PredictionOutput
from .forms import PredictForm
import joblib
import numpy as np

# Create your views here.

@login_required(login_url="common:login")
def predict(request):
    if request.method == "POST":
        form = PredictForm(request.POST)
        if form.is_valid():
            area = form.cleaned_data.get("area")
            PredictionOutput.objects.create(area = area)
            obj = PredictionOutput.objects.last()

            obj_list=[obj.area]

            model_input_list = np.array(obj_list).reshape(1,-1)

            with open("model/pred_xgb_output_with_area_sc_f.pkl", "rb") as f:
                scaler_f = joblib.load(f)
                feature = scaler_f.transform(model_input_list)

            with open("model/pred_xgb_output_with_area.pkl", "rb") as m:
                model = joblib.load(m)
                y_p = model.predict(feature)

            with open("model/pred_xgb_output_with_area_sc_t.pkl", "rb") as t:
                scaler_t = joblib.load(t)
                target_pred = scaler_t.inverse_transform(y_p.reshape(-1,1))

            # if y_p == 1:
            #     y_p = "배추 생산이 가능한 지역으로 예측됩니다."
            # else:
            #     y_p = "배추 생산이 불가능한 지역으로 예측됩니다."

            context= {
                "area":obj.area,
                "form":form,
                "obj_test": target_pred,
            }
            return render(request, "common/result_output.html", context)
    else:
        form = PredictForm()
        user = request.user
        user_info = UserInfo.objects.get(user=user)
        context = {
            "user_info": user_info,
            "form": form,
            "target_pred": None,
        }
        return render(request, "common/recommend_op.html", context)