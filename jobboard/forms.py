from django.forms import ModelForm 
from .models import *
from django import forms


class PostForm(forms.ModelForm):
    
    class Meta:
        model = PostJob
        fields = ('title','description','type_job',
                  'location','salary','gender','vacancy',
                  'requirement')
        
class ApplicationForm(forms.ModelForm):
      
    class Meta :
        model = Application
        fields = ('description','contact_app')
        

        

