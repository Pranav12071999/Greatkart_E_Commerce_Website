from django import forms
from accounts.models import *
from django.core.exceptions import ValidationError
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone_number']
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean() # This will fetch the cleaned data dictionary. 
        email = cleaned_data.get('email')
        email_exists = Account.objects.filter(email=email).exists()
        
        if email_exists:
            raise ValidationError(
                "Email already existed!!"
            )

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError(
                "Password doesn't match with each other."
            )