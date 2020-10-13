from django import forms

from staffmodule.models import Service
from .models import *


class BookingForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Service.objects.all(),
    )
    service_on = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Booking
        fields = ['services', 'service_on',
                  'load_type', 'unit', 'delivery_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['services'].label = "Select your service(s)"
        self.fields['service_on'].label = "When do you need laundry to be done?"
        self.fields['load_type'].label = "What type of Load will it be?"
        self.fields['unit'].label = "How many dress(es) or bag(s) it will be?"
        self.fields['delivery_type'].label = "Delivery Type"
