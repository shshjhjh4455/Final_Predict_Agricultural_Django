from django import forms
from .models import PredictionOutput


class PredictForm(forms.Form):
    area = forms.IntegerField()

    class Meta:
        model = PredictionOutput
        fields = (
            "area",
        )
        