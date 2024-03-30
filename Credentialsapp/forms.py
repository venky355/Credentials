from django import forms
from Credentialsapp.models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User  # Specify the model the form is associated with
        fields = ['username', 'password', 'email']  # Specify fields to include in the form
        # Add other fields as needed for user registration

class DealerRegistrationForm(forms.ModelForm):
    class Meta:
        model = User  # Specify the model the form is associated with
        fields = ['username', 'password', 'email', 'dealer_field']  # Specify fields to include in the form
        # Add other fields as needed for dealer registration

