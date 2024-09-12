from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View,FormView,TemplateView

from.forms import *
from .forms import PersonalDetailsForm,JobDetailsForm
from .models import   User


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


class PersonalDetailsView(FormView):
    form_class = PersonalDetailsForm
    template_name = 'dating/details.html'
    success_url = reverse_lazy('accounts:job_status')

    def get(self, request, *args, **kwargs):
        # Instantiate both forms
        personal_details_form = PersonalDetailsForm(instance=request.user)
        multiple_image_form = Multiple_ImageForm()
        return self.render_to_response({
            'personal_details_form': personal_details_form,
            'multiple_image_form': multiple_image_form,
        })

    def post(self, request, *args, **kwargs):
        personal_details_form = PersonalDetailsForm(request.POST, request.FILES, instance=request.user)
        multiple_image_form = Multiple_ImageForm(request.POST, request.FILES)

    # Check if both forms are valid
        if personal_details_form.is_valid() and multiple_image_form.is_valid():
           personal_details_form.save()  # Save the personal details form

        # Save multiple images
           multiple_images = request.FILES.getlist('multiple_image')
           for image in multiple_images:
              Multiple_Image.objects.create(user=request.user, multiple_image=image)

        # Redirect to success_url after both forms are valid
           return HttpResponseRedirect(self.get_success_url())

    # If forms are invalid, re-render the page with errors
        return self.render_to_response({
          'personal_details_form': personal_details_form,
          'multiple_image_form': multiple_image_form,
    })



    
class JobStatusView(TemplateView):
    template_name = 'dating/job_status.html'
    success_url = reverse_lazy('accounts:job_details')



class JobDetailsView(FormView):
    template_name = 'Dating/job_details.html'
    form_class = JobDetailsForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user.is_authenticated:
            kwargs.update({
                'instance': self.request.user,
                'data': self.request.POST or None,
            })
        else:
            kwargs.update({
                'data': self.request.POST or None,
            })
        return kwargs

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.save()
        return super().form_valid(form)


