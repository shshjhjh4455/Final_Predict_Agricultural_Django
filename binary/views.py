import numpy as np
import pandas as pd
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response


class Prediction(APIView):
    def post(self, request):
        #data = request.data
        # 사용자가 입력한 데이터를 받아옴, location은 사용자가 입력한 값
        # location = request.data['location']
        avr1 = request.data['avr1']
        max1 = request.data['max1']
        min1 = request.data['min1']
        rain1 = request.data['rain1']
        sun1 = request.data['sun1']
        avr2 = request.data['avr2']
        max2 = request.data['max2']
        min2 = request.data['min2']
        rain2 = request.data['rain2']
        sun2 = request.data['sun2']
        avr3 = request.data['avr3']
        max3 = request.data['max3']
        min3 = request.data['min3']
        rain3 = request.data['rain3']
        sun3 = request.data['sun3']

        """원하는 시기의 3개월 기후 데이터를 feature 값으로 넣어줘야 함
            ex) user가 경기도에 살고, 5월부터 배추 농사를 짓고 싶다고 할 때, 
            해당 월의 전년 5월, 6월, 7월의 3개월 기후 데이터를 가지고 적합 여부를 판단"""
        dtree = ApiConfig.model
        PredictionMade = dtree.predict([[avr1, max1, min1, rain1, sun1, avr2, max2, min2, rain2, sun2, avr3, max3, min3, rain3, sun3]])
        response_dict = {"Predicted drug": PredictionMade}
        print(response_dict)
        return Response(response_dict, status=200)

