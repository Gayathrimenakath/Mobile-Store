from django.contrib.auth.models import User
from mobile.models import *
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class AddMobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ['model_name', 'battery_capacity', 'quantity', 'back_cam', 'front_cam', 'screen_size', 'ram', 'price', 'release_data', 'img']




