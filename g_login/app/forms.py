from django import forms 
from .models import Upload
  
class Images(forms.ModelForm): 
  
    class Meta: 
        model = Upload 
        fields = ['img', 'desc'] 