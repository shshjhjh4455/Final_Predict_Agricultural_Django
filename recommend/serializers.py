from rest_framework import serializers
from .models import PredictionMade


class PredictionMadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionMade
        fields = (
            "avr1",
            "max1",
            "min1",
            "rain1",
            "sun1",
            "avr2",
            "max2",
            "min2",
            "rain2",
            "sun2",
            "avr3",
            "max3",
            "min3",
            "rain3",
            "sun3",
        )


