from django import forms
from .models import *


class ServiceForm(forms.ModelForm):
    service = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Service...'}))

    class Meta:
        model = Service
        fields = ['service']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].label = "Services"


class SubServiceForm(forms.ModelForm):
    sub_service = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Sub service...'}))
    price = forms.FloatField(widget=forms.NumberInput())

    class Meta:
        model = Subservice
        fields = ['sub_service', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_service'].label = "Sub Service"
