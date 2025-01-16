from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomerUser

class CustomerUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(required=False,max_length=15, label="Phone Number")
    address = forms.CharField(required=False,max_length=15, label="Address")
    class Meta:
        model = CustomerUser
        fields = ('username','email', 'password1','password2', 'phone_number', 'address')