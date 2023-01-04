import os
import joblib
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .models import PredictionMade
from .serializers import PredictionMadeSerializer
from rest_framework import viewsets
from rest_framework import permissions

MODEL_FILE = os.path.join(settings.MODEL, "xgb_baechoo_bin_classify_jinhyeok.pickle")
model = joblib.load(MODEL_FILE)


class PredictionMadeViewSet(viewsets.ModelViewSet):
    queryset = PredictionMade.objects.all()
    serializer_class = PredictionMadeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


# def index(request):
#     return render(request, "recommend/index.html")


# def predict(request):
#     return render(request, "recommend/predict.html")


def result(request):
    avr1 = request.GET["avr1"]
    max1 = request.GET["max1"]
    min1 = request.GET["min1"]
    rain1 = request.GET["rain1"]
    sun1 = request.GET["sun1"]
    avr2 = request.GET["avr2"]
    max2 = request.GET["max2"]
    min2 = request.GET["min2"]
    rain2 = request.GET["rain2"]
    sun2 = request.GET["sun2"]
    avr3 = request.GET["avr3"]
    max3 = request.GET["max3"]
    min3 = request.GET["min3"]
    rain3 = request.GET["rain3"]
    sun3 = request.GET["sun3"]
    data = [
        [
            float(avr1),
            float(max1),
            float(min1),
            float(rain1),
            float(sun1),
            float(avr2),
            float(max2),
            float(min2),
            float(rain2),
            float(sun2),
            float(avr3),
            float(max3),
            float(min3),
            float(rain3),
            float(sun3),
        ]
    ]
    result = model.predict(data)
    if result[0] == 0:
        result = "배추가 잘 자라지 않을 것 같습니다."
    else:
        result = "배추가 잘 자라실 것 같습니다."
    return render(request, "recommend/result.html", {"result": result})
