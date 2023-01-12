from django.shortcuts import render
from .api import get_candle_df
import pandas as pd
import pickle
from django.shortcuts import render
from .models import Result
from datetime import date
from time import localtime, time
from common.models import UserInfo
from .forms import apicheckerForm
from output.models import PredictionOutput
from django.contrib.auth.decorators import login_required
from .api import check_api


# 예측하는 페이지 전에 보여주는 페이지.
def predict_price(days):

    # Load the model and scalers
    model = pickle.load(
        open("model/price_candle_XGBoost_continuous_{}days.pkl".format(days), "rb")
    )
    scaler1 = pickle.load(open("model/price_candle_scaler1_{}.pkl".format(days), "rb"))
    scaler2 = pickle.load(open("model/price_candle_scaler2_{}.pkl".format(days), "rb"))

    # load df
    candle_df_lasts = get_candle_df().candle_df_lasts

    df = get_candle_df().df

    globals()[f"item_{days}"] = df.tail(days)

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
    return y_pred, globals()[f"item_{days}"]


@login_required(login_url="common:login")
def detail(request):

    today = date.today()
    tm = localtime(time())

    if not Result.objects.filter(date=today).exists():

        obj = PredictionOutput.objects.last()

        pred_list = [1, 2, 3, 4, 5, 10, 20, 60, 120]
        for i in pred_list:
            globals()[f"pred_{i}"] = int(predict_price.y_pred(i)[0])

        for i in pred_list:
            globals()[f"item_{i}"] = predict_price.__getattribute__(f"item_{i}")

        context = Result.objects.create(
            date=today,
            tm=tm.tm_hour,
            item_1=item_1,
            item_2=item_2,
            item_3=item_3,
            item_4=item_4,
            item_5=item_5,
            item_10=item_10,
            item_20=item_20,
            item_60=item_60,
            item_120=item_120,
            pred_1=pred_1,
            pred_2=pred_2,
            pred_3=pred_3,
            pred_4=pred_4,
            pred_5=pred_5,
            pred_10=pred_10,
            pred_20=pred_20,
            pred_60=pred_60,
            pred_120=pred_120,
        )
    elif tm.tm_hour >= 16 and Result.objects.last().tm < 16:

        for i in pred_list:
            globals()[f"pred_{i}"] = int(predict_price.y_pred(i)[0])

        for i in pred_list:
            globals()[f"item_{i}"] = predict_price.__getattribute__(f"item_{i}")

        context = Result.objects.create(
            date=today,
            tm=tm.tm_hour,
            item_1=item_1,
            item_2=item_2,
            item_3=item_3,
            item_4=item_4,
            item_5=item_5,
            item_10=item_10,
            item_20=item_20,
            item_60=item_60,
            item_120=item_120,
            pred_1=pred_1,
            pred_2=pred_2,
            pred_3=pred_3,
            pred_4=pred_4,
            pred_5=pred_5,
            pred_10=pred_10,
            pred_20=pred_20,
            pred_60=pred_60,
            pred_120=pred_120,
        )

    else:
        context = Result.objects.last()
        obj = PredictionOutput.objects.last()
    return render(
        request,
        "common/api_detail.html",
        {
            "context": context,
            "output": PredictionOutput.objects.get(id=obj.id).output,
            "area": PredictionOutput.objects.get(id=obj.id).area,
        },
    )
