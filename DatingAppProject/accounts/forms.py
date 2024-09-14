from .models import User
from django import forms

class UserJobInfoForm(forms.ModelForm):
    
    EXPERTISELEVEL_CHOICES=(('B','Beginner'),('I','Intermediate'),('E','Expert'))
    jobtitle=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type' : 'text'}))
    expertise_level=forms.ChoiceField(choices=EXPERTISELEVEL_CHOICES,widget=forms.Select(attrs={'class':'form-select','type' : 'text'}))
    class Meta:
        model =User
        fields = ["jobtitle","expertise_level"]
class UserRelationShipForm(forms.ModelForm):
    RELATIONSHIP_CHOICES=(('ST','Short Term Relationship'),('LT','Long Term Relationship'))
    APP_CHOICES =(('D','Dating'),('M','Matrimony'))
    relationship_goals=forms.ChoiceField(choices=RELATIONSHIP_CHOICES,widget=forms.CheckboxSelectMultiple(attrs={'class':'form-check-input','type':'checkbox'}))
   
    class Meta:
        model =User
        fields = ["relationship_goals"]
