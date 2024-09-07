from django import forms
from django.core.exceptions import ValidationError

from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



class PersonalDetailsForm (forms.ModelForm):

    class Meta:
        model = User
        fields = ["age","dob","hobbies","interest","drinking_habits",
                  "smoking_habits","qualification","location","profile_picture","multiple_image","short_reel"]
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
                'placeholder': 'Drinking Habit'
            }),
            'smoking_habits': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Smoking Habit'
            }),

            'qualification': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ' Qualification',
            }),
             'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Location'
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #ced4da; padding: 10px;',
                'title': 'Upload Profile Picture',
            }),
            'multiple_image': forms.FileInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #ced4da; padding: 10px;',
                'title': 'Upload Profile Picture',

            }),
            'short_reel': forms.FileInput(attrs={
                'class': 'form-control',
                'style': 'border: 1px solid #ced4da; padding: 10px;',
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
            'multiple_image': ' ',
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
       super(RegisterForm, self).__init__(*args, **kwargs)
       self.fields['hobbies'].empty_label = "Hobby"
       self.fields['interest'].empty_label = "Interest"
       self.fields['qualification'].empty_label = "Qualification"


