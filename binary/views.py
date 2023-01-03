import numpy as np
import pandas as pd
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response


class Prediction(APIView):
    def post(self, request):
        #data = request.data
        # 사용자가 입력한 데이터를 받아옴, location은 사용자가 입력한 값
        location = request.data['location']
        age= request.GET.get('age')
        gender = request.GET.get('gender')
        bp = request.GET.get('bp')
        cholesterol = request.GET.get('cholesterol')
        salt = request.GET.get('salt')
        dtree = ApiConfig.model
        #predict using independent variables
        
        """원하는 시기의 3개월 기후 데이터를 feature 값으로 넣어줘야 함
            ex) user가 경기도에 살고, 5월부터 배추 농사를 짓고 싶다고 할 때, 
            해당 월의 전년 5월, 6월, 7월의 3개월 기후 데이터를 가지고 적합 여부를 판단"""

        PredictionMade = dtree.predict([[avr1, max1, min1, rain1, sun1, avr2, max2, min2, rain2, sun2, avr3, max3, min3, rain3, sun3]])
        response_dict = {"Predicted drug": PredictionMade}
        print(response_dict)
        return Response(response_dict, status=200)

