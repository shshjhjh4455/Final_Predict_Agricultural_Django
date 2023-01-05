from django.shortcuts import render
from django.http import HttpResponse
# from .models import Recommend
import pickle
import joblib
import numpy as np



def predict(request):
    return render(request, 'common/predict.html')

def result(request):
    sc = pickle.load(open('model/xgb_baechoo_bin_classify_jinhyeok.pickle', 'rb'))
    model = joblib.load(open('model/xgb_baechoo_bin_classify_scaler_jinhyeok.pkl', 'rb'))

    val1 = float(request.GET['avr1']),
    val2 = float(request.GET['max1']),
    val3 = float(request.GET['min1']),
    val4 = float(request.GET['rain1']),
    val5 = float(request.GET['sun1']),
    val6 = float(request.GET['avr2']),
    val7 = float(request.GET['max2']),
    val8 = float(request.GET['min2']),
    val9 = float(request.GET['rain2']),
    val10 = float(request.GET['sun2']),
    val11 = float(request.GET['avr3']),
    val12 = float(request.GET['max3']),
    val13 = float(request.GET['min3']),
    val14 = float(request.GET['rain3']),
    val15 = float(request.GET['sun3']),
    
    input_features = np.array([val1, val2, val3, val4, val5, val6, val7, val8, val9, val10, val11, val12, val13, val14, val15])
    pred = model.predict(sc.transform(input_features.reshape(1, -1)))
    result1 = pred
    if pred == [0]:
        result1 = "배추가 잘 자라지 않을 것 같습니다."
    else:
        result1 = "배추가 잘 자라실 것 같습니다."
    return render(request, 'common/result.html', {'result_pred': result1})
