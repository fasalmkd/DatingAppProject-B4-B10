from django import forms
from django.core.exceptions import ValidationError

from .models import User,Multiple_Image
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



class PersonalDetailsForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["age","dob","hobbies","interest","drinking_habits",
                  "smoking_habits","qualification","location","profile_pic","short_reel"]
        widgets = {
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Age',
            }),

            'dob': forms.DateInput(attrs={
                'class': 'form-control',
                'type':'date',
                'placeholder': 'DOB',
            }),
            'hobbies': forms.Select(attrs={
                'class': 'form-control',
            }),

            'interest': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ' Interests',
            }),
            'drinking_habits': forms.Select(attrs={
                'class': 'form-control',
            }),
            'smoking_habits': forms.Select(attrs={
                'class': 'form-control',
            }),

            'qualification': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ' Qualification',
            }),
             'location': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Location'
            }),
            'profile_pic': forms.FileInput(attrs={
                'class': 'form-control',  # Add CSS class
                'style': 'width:100%; padding:10px; border: 1px solid #ccc; border-radius: 5px;',  # Add inline CSS if needed
            }),
            
            'short_reel': forms.FileInput(attrs={
                'class': 'form-control',
                'style': 'width:100%; padding:10px; border: 1px solid #ccc; border-radius: 5px; ',
            }),

        }



        labels = {
            'age': '',
            'dob': ' ',
            'hobbies': ' ',
            'interest': '',
            'drinking_habits': ' ',
            'smoking_habits': '',
            'qualification': ' ',
            'location':' ',
            'profile_picture': '',
            'short_reel': ' ',

        }

        error_messages = {
            'age': {
                'required': '',
            },
            'dob': {
                'required': '',
            },
            'hobbies': {
                'required': '',
            },
            'interest': {
                'required': '',
            },
            'drinking_habits': {
                'required': '',
            },
            'smoking_habits': {
                'required': '',
            },
            'qualification': {
                'required': '',
            }
        }


    def __init__(self, *args, **kwargs):
       super(PersonalDetailsForm, self).__init__(*args, **kwargs)
       self.fields['hobbies'].empty_label = "Hobby"
       self.fields['interest'].empty_label = "Interest"
       self.fields['qualification'].empty_label = "Qualification"
       self.fields['location'].empty_label = "Location"
       self.fields['drinking_habits'].empty_label = "Drinking Habits"
       self.fields['smoking_habits'].empty_label = "Smoking Habits"

       self.fields['drinking_habits'].initial = None


class Multiple_ImageForm(forms.ModelForm):
    class Meta:
        model = Multiple_Image
        fields = ['multiple_image']
        widgets = {
            'multiple_image': forms.FileInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['multiple_image'].widget.attrs.update({'multiple': True})  # Make sure it's 'widget', not 'widgets'







class JobDetailsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['company_name','designation','work_location']
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' Company Name',
            }),

            'designation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ' Designation',
            }),
            'work_location': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ' Work Location',
            }),
        }

        labels = {
            'company_name': '',
            'designation': ' ',
            'work_location': ' ',
        }
    def __init__(self, *args, **kwargs):
       super(JobDetailsForm, self).__init__(*args, **kwargs)
       self.fields['company_name'].empty_label = "Company Name"
       self.fields['designation'].empty_label = "Designation"
       self.fields['work_location'].empty_label = "Work Location"