import os
import joblib
import numpy as np
import pandas as pd
import pickle
import json
import requests
import xgboost as xgb
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from django.db import models
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers.json import Serializer as JSONSerializer
from django.core.serializers.python import Serializer as PythonSerializer
from django.core.serializers.xml_serializer import Serializer as XMLSerializer
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers.json import Serializer as JSONSerializer
from django.core.serializers.python import Serializer as PythonSerializer
from django.core.serializers.xml_serializer import Serializer as XMLSerializer


MODEL_FILE = os.path.join(settings.MODEL, "xgb_baechoo_bin_classify_jinhyeok.pickle")
model = joblib.load(MODEL_FILE)

# xgb_baechoo_bin_classify_scaler_jinhyeok.pickle
# SCALER_FILE = os.path.join(
#     settings.MODEL, "xgb_baechoo_bin_classify_scaler_jinhyeok.pickle"
# )
# std = joblib.load(SCALER_FILE)


# # predict 결과 값을 html로 보여주는 함수


def predict(request):
    # pred_test = [
    #     7.30,
    #     19.80,
    #     -1.70,
    #     53.9,
    #     390.280,
    #     14.1,
    #     28.00,
    #     3.80,
    #     38.50,
    #     496.970,
    #     17.7,
    #     28.50,
    #     8.10,
    #     97.70,
    #     560.500,
    # ]
    # pred_test = np.array(pred_test).reshape(1, -1)
    # pred_test = std.transform(pred_test)
    # predict = model.predict(pred_test)
    # predict = predict[0]
    # print(predict)
    return render(request, "common/recommend.html")
