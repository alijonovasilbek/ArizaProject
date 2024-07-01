from django import forms
from .models import UserInformation

class UserInformationForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = ['first_name','last_name', 'phone_your', 'region', 'class_user']
