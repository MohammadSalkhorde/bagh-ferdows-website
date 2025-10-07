from .models import *
from django import forms


class MemoryForm(forms.ModelForm):
    class Meta:
        model=Memory
        fields=['title','text','photo','memory_date']
       
        widgets = {
            'memory_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',  
            }),
        }
class MemoryGalleryForm(forms.ModelForm):
    class Meta:
        model=MemoryGallery
        fields=['photo']