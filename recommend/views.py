from django.shortcuts import render
from common.models import UserInfo
from django.contrib.auth.decorators import login_required
from .models import PredictionInput
from .forms import PredictForm
from save_csv.models import baechoo_new
import pickle


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

            if obj.month==11:
                bae_1= baechoo_new.objects.get(location= obj.location, month=obj.month)
                bae_2= baechoo_new.objects.get(location= obj.location, month=obj.month+1)
                bae_3= baechoo_new.objects.get(location= obj.location, month=1)
            elif obj.month==12:
                bae_1= baechoo_new.objects.get(location= obj.location, month=obj.month)
                bae_2= baechoo_new.objects.get(location= obj.location, month=1)
                bae_3= baechoo_new.objects.get(location= obj.location, month=2)
            else:
                bae_1= baechoo_new.objects.get(location= obj.location, month=obj.month)
                bae_2= baechoo_new.objects.get(location= obj.location, month=obj.month+1)
                bae_3= baechoo_new.objects.get(location= obj.location, month=obj.month+2)

            obj_list=[bae_1, bae_2, bae_3]
            model_input_list= []

            for i in range(len(obj_list)):
                model_input_list.append(obj_list[i].avr)
                model_input_list.append(obj_list[i].max)
                model_input_list.append(obj_list[i].min)
                model_input_list.append(obj_list[i].rain)
                model_input_list.append(obj_list[i].sun)

            model_input_list = np.array(model_input_list).reshape(1,-1)

            with open("model/xgb_baechoo_bin_classify_scaler_jinhyeok.pkl", "rb") as s:
                scaler = joblib.load(s)
                feature = scaler.transform(model_input_list)

            with open("model/xgb_baechoo_bin_classify_jinhyeok.pickle", "rb") as f:
                model = pickle.load(f)
                y_p = model.predict(feature)

            if y_p == 1:
                y_p = "배추 생산이 가능한 지역으로 예측됩니다."
            else:
                y_p = "배추 생산이 불가능한 지역으로 예측됩니다."


            user = request.user
            user_info = UserInfo.objects.get(user=user)

            context= {
                "user_info":user_info,
                "form":form,
                "obj_test": y_p,
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