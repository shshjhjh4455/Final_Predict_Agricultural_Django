from django import forms
from .models import PredictionInput


class PredictForm(forms.Form):
    location = forms.CharField(label="지역")
    month = forms.IntegerField(error_messages={"required" : "월을 입력해 주세요."},label="월")

    class Meta:
        model = PredictionInput
        fields = (
            "location",
            "month",
        )
        