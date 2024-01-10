# busness_e_commerce_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Make sure to import your CustomUser model

class UserForm(UserCreationForm):
    address_id = forms.IntegerField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    company_name = forms.CharField()
    user_role = forms.IntegerField()

    class Meta:
        model = CustomUser
        fields = ('address_id', 'first_name', 'last_name','username', 'email', 'phone_number', 'company_name', 'user_role', 'password1', 'password2')
