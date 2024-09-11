from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import UserJobInfoForm,UserRelationShipForm


# Create your views here.

class UserFormView(TemplateView):
    template_name="userDetails.html"
    success_url= "/home/"

    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()

        if self.request.user.is_authenticated:

            kwargs.update({
                    'instance':self.request.user,
                    'data':self.request.POST
                    })
        else:
            kwargs.update({'data':self.request.POST or None})    
        return kwargs
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context['first_form'] = kwargs.get('first_form', UserJobInfoForm(prefix='first'))

        context['second_form'] = kwargs.get('second_form', UserRelationShipForm(prefix='second'))
        
        print('final context------------:',context)
        return context
    
    def post(self, request, *args, **kwargs):
        # Initialize the forms with their respective data and prefixes
        first_form = UserJobInfoForm(request.POST, prefix='first') if 'first-jobtitle' in request.POST else UserJobInfoForm(prefix='first')
        second_form = UserRelationShipForm(request.POST, prefix='second') if 'second-relationship_goals' in request.POST else UserRelationShipForm(prefix='second')
        
        # Handle the first form (job title)
        if 'first-jobtitle' in request.POST:
            if first_form.is_valid():
                first_form.save()
                return self.render_to_response(self.get_context_data(first_form=first_form, second_form=second_form))
            else:
                print('-----------------error', first_form.errors)
        
        # Handle the second form (relationship goals)
        elif 'second-relationship_goals' in request.POST:
            print('second_form--------------:',second_form)
            if second_form.is_valid():
                relationship_goal = second_form.cleaned_data['relationship_goals']  # This will return a single value like 'ST'
                print('Selected goal:', relationship_goal)
                second_form.save()
                print('---------------------yesssssssssssssssssssssssssssssss saved')  
                return self.form_valid(second_form)
            else:
                print('-----------------error', second_form.errors)
        
        # If neither form is valid or no post data, re-render the page with form errors
        return self.render_to_response(self.get_context_data(first_form=first_form, second_form=second_form)) 
              
    def form_invalid(self, form):
        # Optionally handle the invalid form case here
        print("Form is invalid", form.errors)
        return super().form_invalid(form)   
    
    