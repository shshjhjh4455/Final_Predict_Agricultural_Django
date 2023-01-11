from django.shortcuts import render
import pickle
import joblib
from common.models import UserInfo
from django.contrib.auth.decorators import login_required
from .models import PredictionOutput
from .forms import PredictForm
from save_csv.models import baechoo_new
import pickle
import numpy as np


# 사용자로 부터 달과 지역을 입력받아서 예측값을 출력
@login_required(login_url="common:login")
def oupredict(request):
        return render(request, "common/output.html")
