from django import forms
from .models import User


class SignupForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'}))
    mobile = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': 'Mobile Number...'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'yourname@example.com'}))
    address = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Address..'}))
    street = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Street..'}))
    city = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'City...'}))
    state = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'State...'}))
    pincode = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': 'Pincode...'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Must be at least 8+ charaters'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Retype Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'mobile',
                  'email', 'password', 'confirm_password', 'profile_pic', 'address', 'street', 'city', 'state', 'pincode']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_pic'].label = "Profile Picture"
        self.fields['mobile'].label = "Mobile Number"
        self.fields['email'].label = "Email Address"
        self.fields['first_name'].label = "First Name"
        self.fields['address'].label = "Address"
        self.fields['street'].label = "Street"
        self.fields['city'].label = "City"
        self.fields['state'].label = "State"
        self.fields['pincode'].label = "Pincode"
        self.fields['last_name'].label = "Last Name"
        self.fields['last_name'].required = False

    # validating the email
    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        return email

    # validating the mobile no
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not len(mobile) == 10:
            raise forms.ValidationError('Enter a valid Mobile Number')
        return mobile

    # validating the password
    def clean_password(self):
        password = self.cleaned_data.get('password')
        upper = lower = num = 0
        for i in password:
            if i.isupper():
                upper += 1
            elif i.islower():
                lower += 1
            elif i.isnumeric():
                num += 1
        if not len(password) >= 8:
            raise forms.ValidationError(
                'Your password must be atleast 8 characters')
        if not upper:
            raise forms.ValidationError(
                'Your password must have atleast 1 UPPERCASE')
        if not lower:
            raise forms.ValidationError(
                'Your password must have atleast 1 lowercase')
        if not num:
            raise forms.ValidationError(
                'Your password must have atleast 1 Numeric [0-9]')
        return password

    # validating the confirm password field
    def clean_confirm_password(self):
        confirm = self.cleaned_data.get('confirm_password')
        if not confirm == self.cleaned_data.get('password'):
            raise forms.ValidationError('Your password does not match')
        return confirm


class SigninForm(forms.Form):
    mobile = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': 'Enter your Mobile Number'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Must be at least 8+ charaters'}
    ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mobile'].label = "Mobile Number"


class MyaccountForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'}))
    mobile = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': 'Enter your Mobile Number'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'yourname@example.com'}))
    address = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Address..'}))
    street = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Street..'}))
    city = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'City...'}))
    state = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'State...'}))
    pincode = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': 'Pincode...'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'mobile', 'email',
                  'address', 'street', 'city', 'state', 'pincode']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mobile'].label = "Mobile Number"
        self.fields['email'].label = "Email Address"
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['address'].label = "Address"
        self.fields['street'].label = "Street"
        self.fields['city'].label = "City"
        self.fields['state'].label = "State"
        self.fields['pincode'].label = "Pincode"
        self.fields['last_name'].required = False

    # validating the email
    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        return email

    # validating the mobile no
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not len(mobile) == 10:
            raise forms.ValidationError('Enter a valid Mobile Number')
        return mobile
