from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.messages import success, error
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm
# Create your views here.

class LoginView(View):
  
  def get(self, request):
    login_form = LoginForm()
    return render(request, 'login.html', {'login_form':login_form})

  def post(self, request):
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
      cd = login_form.cleaned_data
      user = authenticate(request, email=cd['email'], password=cd['password'])
      if user:
        login(request, user)
        success(request, message="You logged in with successfully", extra_tags='success')
        return redirect('home_url')
      else:
        error(request, message="The user with entry information not found", extra_tags='danger')
        return redirect('account:login_url')
    error(request, message="Fill all the field then click on submit button", extra_tags='danger')
    return redirect('account:login_url')

class RegisterView(View):

  def get(self, request):
    register_form = RegisterForm()
    return render(request, 'register.html', {'register_form':register_form})

  def post(self, request):
    register_form = RegisterForm(request.POST)
    if register_form.is_valid():
      register_form.save()
      success(request, message="Your account created with successfully!", extra_tags='success')
      return redirect('account:login_url')
    error(request, message="Fill all the field then click on submit button", extra_tags='danger')
    return redirect('account:register_url')