from django import forms
from .models import Message

class contact(forms.ModelForm):
    class Meta:
        model=Message
        fields=['full_name','email','title_message','text']

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی خود را وارد کنید'}),
            'email': forms.EmailInput(attrs={'placeholder': 'مثال : garden@example.com'}),
            'title_message': forms.TextInput(attrs={'placeholder': 'عنوان پیام'}),
            'text': forms.Textarea(attrs={'placeholder': 'متن پیام'}),
        }