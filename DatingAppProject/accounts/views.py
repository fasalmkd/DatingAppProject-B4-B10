from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View,FormView,TemplateView

from.forms import *
from .forms import PersonalDetailsForm
from .models import   User


# Create your views here.

class PersonalDetailsView(FormView):
    form_class = PersonalDetailsForm 
    template_name = 'dating/details.html'
    success_url = reverse_lazy('new_app:job_status')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user.is_authenticated:
            kwargs.update({
                'instance': self.request.user,
                'data':self.request.POST or None,
            })
        else:
            kwargs.update({
                'data': self.request.POST or None,
            })
        return kwargs

    def form_valid(self,form):
        if self.request.user.is_authenticated:
            form.save()
        return super().form_valid(form)

    

# Create your views here.
class JobStatusView(TemplateView):
    template_name = 'dating/job_status.html'
    success_url = reverse_lazy('new_app:job_details')
