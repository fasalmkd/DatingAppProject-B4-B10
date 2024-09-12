from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,FormView,TemplateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as AuthLoginView
from accounts.forms import EmailOrMobileAuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import *
from django.contrib import messages
from .models import User
from django.core.mail import send_mail
from django.contrib.auth.views import PasswordResetView,PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin




# # Create your views here.


class HomeView(TemplateView):
    template_name = 'accounts/home.html'

class SignupView(FormView):
    model=User
    template_name= 'accounts/signup.html'
    form_class = UserCreationForm
    success_url=reverse_lazy('accounts:details')

    def form_valid(self, form):
    # Validate and clean passwords using the form's validation methods
        password = form.cleaned_data.get('password')
        confirm_password = form.cleaned_data.get('confirm_password')

    # Check if passwords match
        if password and confirm_password and password != confirm_password:
            form.add_error('confirm_password', "Passwords do not match.")
            return self.form_invalid(form)

    # Save the user instance, but don't commit to the database yet
        user = form.save(commit=False)

    # Set the password using set_password to ensure it is hashed
        user.set_password(password)
        user.save()  # Now save the user to the database

    # Specify the custom authentication backend
        backend = 'accounts.backends.EmailOrMobileBackend'
    
    # Log the user in using the custom backend
        login(self.request, user, backend=backend)
    
    # Redirect to the success URL
        return redirect(self.success_url)

class LoginView(AuthLoginView):
    template_name = 'accounts/login.html'
    form_class = EmailOrMobileAuthenticationForm
    success_url = reverse_lazy('accounts:details')

    def form_valid(self, form):
        user = form.get_user()
        backend = 'accounts.backends.EmailOrMobileBackend'
        login(self.request, user, backend=backend)
        return redirect(self.success_url)



class DetailsView(TemplateView):
    template_name = 'accounts/details.html'
   

