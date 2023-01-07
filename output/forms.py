from django import forms
from .models import PredictionOutput


class outputForm(forms.Form):
    area = forms.IntegerField()

    class Meta:
        model = PredictionOutput
        fields = (
            "area",
        )
        