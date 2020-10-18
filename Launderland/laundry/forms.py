from django import forms
from datetime import date, datetime

from staffmodule.models import Service
from .models import *


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['services', 'quantity', 'delivery_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['services'].label = "Select your service"
        self.fields['quantity'].label = "How many dress(es) will it be?"
        self.fields['delivery_type'].label = "Delivery Type"

    def clean_service_on(self):
        service_on = self.cleaned_data.get('service_on')
        diff = service_on - date.today()
        diff = diff.days
        if service_on == date.today() and datetime.now().hour > 20:
            raise forms.ValidationError(
                'Sorry! Try Tomorrow. Before 8 pm')
        if diff < 0:
            raise forms.ValidationError('Please Enter a Valid Date!')
        if diff > 7:
            raise forms.ValidationError(
                'Bookings are allowed only 7 days prior')
        return service_on
