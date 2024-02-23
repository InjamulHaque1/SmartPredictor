from django import forms
from .models import UserProfile

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'age', 'address', 'mobile', 'gender']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean(self):
        cleaned_data = super().clean()

class LoginForm(forms.Form):
    u_name = forms.CharField(label='Username', max_length=100)
    u_password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
