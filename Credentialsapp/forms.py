from django import forms
from Credentialsapp.models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User  
        fields = ['username', 'password', 'email']  
        

class DealerRegistrationForm(forms.ModelForm):
    class Meta:
        model = User  
        fields = ['username', 'password', 'email', 'dealer_field']  
