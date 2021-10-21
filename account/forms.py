from django import forms
from django.forms import widgets

from .models import CustomUser

class LoginForm(forms.Form):

  email = forms.CharField(
    max_length=50,
    min_length=8,
    label="Email",
    widget=forms.EmailInput(attrs={'class':'form-control', 'name':'email', 'id':'email', 'placeholder':'Enter your email address'})
  )
  password = forms.CharField(
    min_length=5,
    max_length=12,
    label="Password",
    widget=forms.PasswordInput(attrs={'class':'form-control', 'name':'password', 'id':'password', 'placeholder':'Enter your password'})
  )


class RegisterForm(forms.ModelForm):

  password = forms.CharField(
    max_length=12,
    min_length=5,
    help_text="Fill input with min 5 and max 12 characters",
    widget=forms.PasswordInput(attrs={
      'class': 'form-control my-2',
      'placeholder': 'Enter your password',
      'id': 'password',
      'name': 'password'
    })
  )
  password2 = forms.CharField(
    max_length=12,
    min_length=5,
    help_text="Fill input with min 5 and max 12 characters",
    label="Re-password",
    widget=forms.PasswordInput(attrs={
      'class': 'form-control my-2',
      'placeholder': 'Enter your password again',
      'id': 'password2',
      'name': 'password2'
    })
  )

  class Meta:
    model = CustomUser
    fields = ('email', 'phone_number')
    widgets = {
      'email': forms.EmailInput(attrs={'class':'form-control my-2', 'placeholder':'Enter your email address'}),
      'phone_number': forms.NumberInput(attrs={'class':'form-control my-2', 'placeholder':'Enter your phone number'})
    }

  def clean(self):
    cd = super().clean()
    if cd['password'] and cd['password2'] and cd['password'] != cd['password2']:
      raise forms.ValidationError('Your password and its repeat does not match')
    return cd

  def save(self, commit=True):
    cd = self.cleaned_data
    instance = super().save(commit=False)
    instance.set_password(cd['password'])
    if commit:
      super().save(commit=True)