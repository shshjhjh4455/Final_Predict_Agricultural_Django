import os
import joblib
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .models import PredictionMade
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


MODEL_FILE = os.path.join(settings.MODEL, "xgb_baechoo_bin_classify_jinhyeok.pickle")
model = joblib.load(MODEL_FILE)

# using model to predict the result of the data from the user_info.location
# using user_info.location to search the data from the database() and get the data 
def predict_result(location):
    result = model.predict(location)
    return result



