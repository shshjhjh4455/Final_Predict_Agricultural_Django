from django.shortcuts import render
from .api import get_candle_df
import json
import pandas as pd
import pickle
import numpy as np
import datetime
from django.shortcuts import render
from .models import Result
from datetime import date

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

def detail(request):
    today = date.today()
    if not Result.objects.filter(date=today).exists():
        pred_5 = int(predict_price(5)[0])
        pred_10 = int(predict_price(10)[0])
        pred_20 = int(predict_price(20)[0])
        pred_60 = int(predict_price(60)[0])
        pred_120 = int(predict_price(120)[0])

        context = Result.objects.create(date=today,pred_5=pred_5, pred_10=pred_10, pred_20=pred_20, pred_60=pred_60, pred_120=pred_120)
    else:
        context = Result.objects.filter(date=today).first()
    return render(request, 'common/api_detail.html', {'context': context})

