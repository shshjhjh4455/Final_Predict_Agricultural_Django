from django import forms
from .models import PredictionOutput


class PredictForm(forms.Form):
    area = forms.IntegerField(label="면적")

    class Meta:
        model = PredictionOutput
        fields = (
            "area",
        )