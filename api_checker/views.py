from django.shortcuts import render
from .api import check_api, create_candles, get_candle_df
import json
import pandas as pd
import pickle
import numpy as np
import datetime

# 예측하는 페이지 전에 보여주는 페이지.
@login_required(login_url="common:login")
def predict_price(request, days):
  # Load the model and scalers

    if request.method == "POST":
        model = pickle.load(open('model/price_candle_XGBoost_continuous_{}days.pkl'.format(days), 'rb'))
        scaler1 = pickle.load(open('model/price_candle_scaler1_{}.pkl'.format(days), 'rb'))
        scaler2 = pickle.load(open('model/price_candle_scaler2_{}.pkl'.format(days), 'rb'))

        candle_df_last_x = get_candle_df()

        # Select the last `days` days of data
        candle_df_last_x = candle_df_lasts[days]

        # Drop the '종가_shift' column
        candle_df_last_x = candle_df_last_x.drop(f'{days}종가_shift')

        # Convert candle_df_last_x to a Pandas dataframe
        candle_df_last_x = pd.DataFrame(candle_df_last_x)
        candle_df_last_x= candle_df_last_x.T

        # Model predict using test_data
        test_data_sc = scaler1.transform(candle_df_last_x)
        test_data_sc = pd.DataFrame(test_data_sc, columns=candle_df_last_x.columns, index=candle_df_last_x.index)
        y_pred = model.predict(test_data_sc)

        # reshape y_pred
        y_pred = y_pred.reshape(-1,1)

        # Inverse transform y_pred
        y_pred = scaler2.inverse_transform(y_pred)

        context = {"predict" : y_pred[1]}

        # Return the predicted values
        return render(request, "")

    else:
        form = PredictForm()
        user = request.user
        user_info = UserInfo.objects.get(user=user)
        context = {
            "user_info": user_info,
            "form": form,
            "target_pred": None,
        }
        return render(request, "common/recommend_op.html", context)

# def index(request):
#     res = check_api()
#     return render(request, 'common/predict.html')

# def detail(request):
#     res = check_api()
#     # res를 dict로 바꿔서 context에 넣어준다.
#     context = {'res': res}
#     return render(request, 'common/api_detail.html', context)


