import os
import joblib
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

# Create your views here.
MODEL_FILE = os.path.join(settings.MODEL, "xgb_baechoo_bin_classify_jinhyeok.pickle")
model = joblib.load(MODEL_FILE)

# avr1,max1,min1,rain1,sun1,avr2,max2,min2,rain2,sun2,avr3,max3,min3,rain3,sun3

# predict 결과 값을 html로 보여주는 함수
@csrf_exempt
@require_POST

def predict(request):
    result = model.predict(
        [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
    )
    return render(request, "recommend/predict.html", {"result": result})
