from django import forms

from staffmodule.models import *
from .models import *


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['services', 'sub_service', 'quantity', 'delivery_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['services'].label = "Select your service"
        self.fields['sub_service'].label = "What mode do you prefer"
        self.fields['quantity'].label = "How many dress(es) will it be?"
        self.fields['delivery_type'].label = "Delivery Type"

        if 'services' in self.data:
            try:
                service = int(self.data.get('services'))
                self.fields['sub_service'].queryset = Subservice.objects.filter(
                    service=service).order_by('sub_service')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['sub_service'].queryset = self.instance.field.sub_service_set.order_by(
                'service')


class UpdateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UpdateBookingForm, self).__init__(*args, **kwargs)


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_mode']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        self.fields['payment_mode'].label = "Mode of Payment :"
