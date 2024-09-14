from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import UserJobInfoForm,UserRelationShipForm
from django.urls import reverse_lazy


# Create your views here.

class UserJobRelationshipView(TemplateView):
    tempalte_name = 'userDetails.html'
    success_url = reverse_lazy('/')
    def get_template_names(self):
        return ['userDetails.html']
   

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        context['job_form'] = UserJobInfoForm()
        context['relationship_form'] = UserRelationShipForm()

        context['first_form_submitted'] = self.request.session.get('first_form_submitted',False)
        return context
    
    def post(self, request, *args, **kwargs):
        print('yes posted')
        print(request.POST)
        print('request session 1', request.session )
        job_form =UserJobInfoForm()
        relationship_form=UserRelationShipForm()
        if 'expertise_level' in request.POST:
            print('list of expertise_level from expertise_level',request.POST.get('expertise_level'))
            print('list of expertise_level from expertise_level',request.POST.getlist('expertise_level'))
            
            job_form = UserJobInfoForm(request.POST)
            if job_form.is_valid():
                print('request session 2', request.session )
                request.session['job_form_data'] = job_form.cleaned_data
                request.session['first_form_submitted'] = True
                print('request session 3', request.session['job_form_data'])
                print('request session 4', request.session['first_form_submitted'])
            else:
                return self.render_to_response(self.get_context_data(job_form=job_form))  
        elif 'relationship_goals' in request.POST:
            print('request.post for relationship_form_submit ',request.POST)
            print('list of relationship from relationship_goals',request.POST.getlist('relationship_goals'))
            print('list of relationship from relationship_goals',request.POST.get('relationship_goals'))
            relationship_goals = request.POST.get('relationship_goals')
            relationship_form=UserRelationShipForm(request.POST)
            
            job_form_data = request.session.get('job_form_data')
            print('lets take job form data:',job_form_data)
            if not job_form_data:
                print('no job form data')
                return redirect('/')
            
            combined_data = {**job_form_data}
                
            print('combined data',combined_data)
            User.objects.create(**combined_data,relationship_goals=relationship_goals)
            
            print('yes created')

            request.session.pop('job_form_data',None)
            request.session.pop('first_form_submitted',None)
            print('all sucessfull')
            
          
            
        return self.render_to_response(self.get_context_data(job_form=job_form,relationship_form=relationship_form))     
        
    def form_invalid(self, form):
        print("Form is invalid", form.errors)
        return super().form_invalid(form) 
 