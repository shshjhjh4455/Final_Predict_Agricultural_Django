from django import forms
from .models import PredictionOutput


class PredictForm(forms.Form):
    area = forms.IntegerField(label="월")

    class Meta:
        model = PredictionInput
        fields = (
            "location",
            "month",
        )