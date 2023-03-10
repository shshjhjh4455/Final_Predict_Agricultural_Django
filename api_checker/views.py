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
from .models import Result


# 예측하는 페이지 전에 보여주는 페이지.
def predict_price(days=1):

    # Load the model and scalers
    model = pickle.load(
        open("model/price_candle_XGBoost_continuous_{}days.pkl".format(days), "rb")
    )
    scaler1 = pickle.load(open("model/price_candle_scaler1_{}.pkl".format(days), "rb"))
    scaler2 = pickle.load(open("model/price_candle_scaler2_{}.pkl".format(days), "rb"))

    # load df
    candle_df_lasts, df_orgin_list = get_candle_df()

    item_5 = df_orgin_list[-5:]
    item_20 = df_orgin_list[-20:]
    item_365 = df_orgin_list

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
    return y_pred, item_5, item_20, item_365


@login_required(login_url="common:login")
def detail(request):

    today = date.today()
    tm = localtime(time())

    if not Result.objects.filter(date=today).exists():

        obj = PredictionOutput.objects.last()

        pred_1 = int(predict_price(1)[0])
        pred_2 = int(predict_price(2)[0])
        pred_3 = int(predict_price(3)[0])
        pred_4 = int(predict_price(4)[0])
        pred_5 = int(predict_price(5)[0])
        pred_10 = int(predict_price(10)[0])
        pred_20 = int(predict_price(20)[0])
        pred_60 = int(predict_price(60)[0])
        pred_120 = int(predict_price(120)[0])

        item_5 = predict_price(1)[1]
        item_20 = predict_price(1)[2]
        item_365 = predict_price(1)[3]

        context = Result.objects.create(
            date=today,
            tm=tm.tm_hour,
            item_5=item_5,
            item_20=item_20,
            item_365=item_365,
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

        pred_1 = int(predict_price(1)[0])
        pred_2 = int(predict_price(2)[0])
        pred_3 = int(predict_price(3)[0])
        pred_4 = int(predict_price(4)[0])
        pred_5 = int(predict_price(5)[0])
        pred_10 = int(predict_price(10)[0])
        pred_20 = int(predict_price(20)[0])
        pred_60 = int(predict_price(60)[0])
        pred_120 = int(predict_price(120)[0])

        item_5 = predict_price(1)[1]
        item_20 = predict_price(1)[2]
        item_365 = predict_price(1)[3]

        context = Result.objects.create(
            date=today,
            tm=tm.tm_hour,
            item_5=item_5,
            item_20=item_20,
            item_365=item_365,
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
            "item_5": Result.objects.last().item_5,
            "item_20": Result.objects.last().item_20,
            "item_365": Result.objects.last().item_365,
            "output": PredictionOutput.objects.get(id=obj.id).output,
            "area": PredictionOutput.objects.get(id=obj.id).area,
        },
    )
