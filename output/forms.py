from django import forms
from .models import PredictionInput


class PredictForm(forms.Form):
    area = forms.IntegerField(label="면적")

    class Meta:
        model = PredictionInput
        fields = ("area",)
