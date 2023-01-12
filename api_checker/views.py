from django.shortcuts import render
<<<<<<< HEAD
<<<<<<< HEAD
from .api import get_candle_df, check_api
import json
=======
from .api import get_candle_df, make_chart
>>>>>>> parent of 2ba223b8 (차트 띄우기2)
=======
from .api import get_candle_df, make_chart
>>>>>>> parent of 2ba223b8 (차트 띄우기2)
import pandas as pd
import pickle
import numpy as np
from django.shortcuts import render
from .models import Result
from datetime import date
from time import time
from time import localtime


# 예측하는 페이지 전에 보여주는 페이지.
def predict_price(days):

    # Load the model and scalers
    model = pickle.load(
        open("model/price_candle_XGBoost_continuous_{}days.pkl".format(days), "rb")
    )
    scaler1 = pickle.load(open("model/price_candle_scaler1_{}.pkl".format(days), "rb"))
    scaler2 = pickle.load(open("model/price_candle_scaler2_{}.pkl".format(days), "rb"))

    # load df
    candle_df_lasts = get_candle_df()

    # Select the last `days` days of data
    candle_df_last_x = candle_df_lasts[days]

    # Drop the '종가_shift' column
    candle_df_last_x = candle_df_last_x.drop(f"{days}종가_shift")

    # Convert candle_df_last_x to a Pandas dataframe
    candle_df_last_x = pd.DataFrame(candle_df_last_x)
    candle_df_last_x = candle_df_last_x.T

    # Model predict using test_data
    test_data_sc = scaler1.transform(candle_df_last_x)
    test_data_sc = pd.DataFrame(
        test_data_sc, columns=candle_df_last_x.columns, index=candle_df_last_x.index
    )
    y_pred = model.predict(test_data_sc)

    # reshape y_pred
    y_pred = y_pred.reshape(-1, 1)

    # Inverse transform y_pred
    y_pred = scaler2.inverse_transform(y_pred)

    # Return the predicted values
    return y_pred


def index(request):
    return render(request, "common/predict.html")

# def detail(request):
#     date_string = value.strftime("%Y-%m-%d")
#     date_object = datetime.date.fromisoformat(date_string)
#     if not Result.objects.filter(date=date_object).exists():
#         pred_5 = predict_price(5)
#         pred_10 = predict_price(10)
#         pred_20 = predict_price(20)
#         pred_60 = predict_price(60)
#         pred_120 = predict_price(120)

#         context = Result.objects.create(date=today,pred_5=pred_5, pred_10=pred_10, pred_20=pred_20, pred_60=pred_60, pred_120=pred_120)
#     else:
#         context = Result.objects.filter(date=today).first()
#     return render(request, 'common/api_detail.html', {'context': context})

# def detail(request):
#     date_string = value
#     date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()
#     if not Result.objects.filter(date=date_object).exists():
#         pred_5 = predict_price(5)
#         pred_10 = predict_price(10)
#         pred_20 = predict_price(20)
#         pred_60 = predict_price(60)
#         pred_120 = predict_price(120)

#         context = Result.objects.create(date=date_object,pred_5=pred_5, pred_10=pred_10, pred_20=pred_20, pred_60=pred_60, pred_120=pred_120)
#     else:
#         context = Result.objects.filter


# def detail(request):
#     # date 다름 또는 시간이 4시를 넘거나 또는 생성된 객체가 없거나
#     #today = datetime.datetime.now()
#     #today_str= today.strftime('%Y-%m-%d')
#     #obj= Result.objects.get(pk=1)

#     # if not Result.objects.first().exists() or today_str != obj.date:
#     #     pred_5 = predict_price(5)
#     #     pred_10 = predict_price(10)
#     #     pred_20 = predict_price(20)
#     #     pred_60 = predict_price(60)
#     #     pred_120 = predict_price(120)

#     #     context = Result.objects.create(date=today_str,pred_5=pred_5, pred_10=pred_10, pred_20=pred_20, pred_60=pred_60, pred_120=pred_120)
#     # else:
#     #     context = Result.objects.filter(date=today_str).first()
#     return render(request, 'common/api_detail.html')
def detail(request):
    today = date.today()
    tm= localtime(time())

<<<<<<< HEAD
=======
    for root, dirs, files in os.walk("/static/images"):
        for f in files:
            if f == "price_baechoo_"+str(datetime.datetime.today().strftime("%Y_%m_%d"))+".png":
                chart = make_chart()

>>>>>>> parent of 2ba223b8 (차트 띄우기2)
    if not Result.objects.filter(date=today).exists():
        pred_5 = int(predict_price(5)[0])
        pred_10 = int(predict_price(10)[0])
        pred_20 = int(predict_price(20)[0])
        pred_60 = int(predict_price(60)[0])
        pred_120 = int(predict_price(120)[0])

        context = Result.objects.create(date=today, tm= tm.tm_hour, pred_5=pred_5, pred_10=pred_10, pred_20=pred_20, pred_60=pred_60, pred_120=pred_120)
    
    elif tm.tm_hour >= 16 and Result.objects.last().tm < 16:
        pred_5 =int( predict_price(5)[0])
        pred_10 = int(predict_price(10)[0])
        pred_20 = int(predict_price(20)[0])
        pred_60 = int(predict_price(60)[0])
        pred_120 = int(predict_price(120)[0])
        context = Result.objects.create(date=today, tm= tm.tm_hour, pred_5=pred_5, pred_10=pred_10, pred_20=pred_20, pred_60=pred_60, pred_120=pred_120)

    else:
        context = Result.objects.last()
    return render(request, 'common/api_detail.html', {'context': context})

def chart(request):
    df= check_api()
    df_5= df.tail(5)
    df_20= df.tail(20)
    val1= df_5['가격'].to_list()
    val2= df_20['가격'].to_list()
    val3= df['가격'].to_list()
    idx1= df_5.index.to_list()
    idx2= df_20.index.to_list()
    idx3= df.index.to_list()
    context={
        "val1":val1,
        "val2":val2,
        "val3":val3,
        "idx1":idx1,
        "idx2":idx2,
        "idx3":idx3, 
    }
    return render(request, 'common/api_chart.html', context)
