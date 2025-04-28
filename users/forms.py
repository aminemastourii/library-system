from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class BorrowerSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')    


class CompleteProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)