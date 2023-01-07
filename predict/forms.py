from django import forms
from .models import Predictiprice


class PredictpriceForm(forms.Form):
    area = forms.IntegerField()

    class Meta:
        model = Predictiprice
        fields = (
            "area",
        )
        