from django import forms
from .models import Result


class apicheckerForm(forms.Form):
    area = forms.IntegerField(label="면적")

    class Meta:
        model = Result
        fields = (
            "area",
        )
        