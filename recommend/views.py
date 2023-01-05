from django.shortcuts import render, redirect
from recommend.models import PredictionInput
from recommend.forms import PredictForm
from save_csv.models import baechoo_new
from rest_framework import viewsets
import pickle
import numpy as np

def predict(request):
    if request.method == "POST":
        form= PredictForm(request.POST)
        if form.is_valid():
            location= form.cleaned_data.get("location")
            month= form.cleaned_data.get("month")
            PredictionInput.objects.create(
                location=location, month=month
            )
            obj= PredictionInput.objects.last()
            print(obj)
            
            return redirect("recommend/result.html")
    else:
        form = PredictForm()
        return render(request, "recommend/predict.html", {"form": form})
