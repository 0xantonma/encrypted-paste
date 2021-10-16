from django import forms
from .models import Texts


class TextForm(forms.ModelForm):
    class Meta:
        model = Texts
        fields = [
            "text"
        ]


