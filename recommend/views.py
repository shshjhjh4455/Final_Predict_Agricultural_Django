from django.shortcuts import render
from django.http import HttpResponse
from .models import PredictionMade
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


<<<<<<< HEAD
MODEL_FILE = os.path.join(settings.MODEL, "xgb_baechoo_bin_classify_jinhyeok.pickle")
model = joblib.load(MODEL_FILE)

# using model to predict the result of the data from the user_info.location
# using user_info.location to search the data from the database() and get the data 
def predict_result(location):
    result = model.predict(location)
    return result
=======

class PredictionMadeViewSet(viewsets.ModelViewSet):
    queryset = PredictionMade.objects.all()
    serializer_class = PredictionMadeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()
>>>>>>> parent of e2cfe84e (recommend setting)

    def perform_update(self, serializer):
        serializer.save()

<<<<<<< HEAD

=======
    def perform_destroy(self, serializer):
        serializer.delete()

    def get_queryset(self):
        queryset = PredictionMade.objects.all()
        avr1 = self.request.query_params.get("avr1", None)
        max1 = self.request.query_params.get("max1", None)
        min1 = self.request.query_params.get("min1", None)
        rain1 = self.request.query_params.get("rain1", None)
        sun1 = self.request.query_params.get("sun1", None)
        avr2 = self.request.query_params.get("avr2", None)
        max2 = self.request.query_params.get("max2", None)
        min2 = self.request.query_params.get("min2", None)
        rain2 = self.request.query_params.get("rain2", None)
        sun2 = self.request.query_params.get("sun2", None)
        avr3 = self.request.query_params.get("avr3", None)
        max3 = self.request.query_params.get("max3", None)
        min3 = self.request.query_params.get("min3", None)
        rain3 = self.request.query_params.get("rain3", None)
        sun3 = self.request.query_params.get("sun3", None)
        if avr1 is not None:
            queryset = queryset.filter(avr1=avr1)
        if max1 is not None:
            queryset = queryset.filter(max1=max1)
        if min1 is not None:
            queryset = queryset.filter(min1=min1)
        if rain1 is not None:
            queryset = queryset.filter(rain1=rain1)
        if sun1 is not None:
            queryset = queryset.filter(sun1=sun1)
        if avr2 is not None:
            queryset = queryset.filter(avr2=avr2)
        if max2 is not None:
            queryset = queryset.filter(max2=max2)
        if min2 is not None:
            queryset = queryset.filter(min2=min2)
        if rain2 is not None:
            queryset = queryset.filter(rain2=rain2)
        if sun2 is not None:
            queryset = queryset.filter(sun2=sun2)
        if avr3 is not None:
            queryset = queryset.filter(avr3=avr3)
        if max3 is not None:
            queryset = queryset.filter(max3=max3)
        if min3 is not None:
            queryset = queryset.filter(min3=min3)
        if rain3 is not None:
            queryset = queryset.filter(rain3=rain3)
        if sun3 is not None:
            queryset = queryset.filter(sun3=sun3)
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return PredictionMadeSerializer
        elif self.action == "create":
            return PredictionMadeSerializer
        elif self.action == "retrieve":
            return PredictionMadeSerializer
        elif self.action == "update":
            return PredictionMadeSerializer
        elif self.action == "partial_update":
            return PredictionMadeSerializer
        elif self.action == "destroy":
            return PredictionMadeSerializer

    def get_permissions(self):
        if self.action == "list":
            return [permissions.AllowAny()]
        elif self.action == "create":
            return [permissions.AllowAny()]
        elif self.action == "retrieve":
            return [permissions.AllowAny()]
        elif self.action == "update":
            return [permissions.AllowAny()]
        elif self.action == "partial_update":
            return [permissions.AllowAny()]
        elif self.action == "destroy":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def get_serializer_context(self):
        context = super(PredictionMadeViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context
>>>>>>> parent of e2cfe84e (recommend setting)
