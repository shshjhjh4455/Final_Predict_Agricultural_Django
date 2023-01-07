from django.shortcuts import render
import pickle
import joblib
from common.models import UserInfo
from django.contrib.auth.decorators import login_required
from .models import Predictiprice
from .forms import PredictpriceForm
from save_csv.models import baechoo_new
import pickle
import numpy as np


# 임의의 값
@login_required(login_url="common:login")
def price(request):
        return render(request, "common/predict.html")
