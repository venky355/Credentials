
from .models import Product, Wishlist
from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    is_dealer = forms.BooleanField(label='Are you a dealer?', required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_dealer', 'dealer_details']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
            'dealer_details': 'Dealer Details (if applicable)',
        }

    def clean(self):
        cleaned_data = super().clean()
        is_dealer = cleaned_data.get('is_dealer')
        dealer_details = cleaned_data.get('dealer_details')

        if is_dealer and not dealer_details:
            raise forms.ValidationError('Dealer details are required for dealer registration')

        return cleaned_data
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'country', 'quantity', 'price', 'image_url']

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = []