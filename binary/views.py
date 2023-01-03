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
        PredictionMade = dtree.predict([[age, gender, cholesterol, bp, salt]])
        response_dict = {"Predicted drug": PredictionMade}
        print(response_dict)
        return Response(response_dict, status=200)

