from django import forms
from .models import PredictionInput


class PredictForm(forms.Form):
    location = forms.CharField(label="지역")
    month = forms.DateField(label="월")

    class Meta:
        model = PredictionInput
        fields = (
            "location",
            "month",
        )
