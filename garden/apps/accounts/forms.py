from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


#------------------------------------------------------------------------------------------------------------
class RegisterUserForm(forms.ModelForm):
    first_name=forms.CharField(label='نام',widget=forms.TextInput(attrs={"placeholder":'نام را وارد کنید'}))
    last_name=forms.CharField(label='نام خانوادگی',widget=forms.TextInput(attrs={"placeholder":'نام خانوادگی را وارد کنید'}))
    username=forms.CharField(label='نام کاربری',widget=forms.TextInput(attrs={"placeholder":'نام کاربری را وارد کنید'}))
    password1=forms.CharField(label='رمز عبور',widget=forms.PasswordInput(attrs={"placeholder":'رمز عبور را وارد کنید'}))
    password2=forms.CharField(label='تکرار رمز عبور',widget=forms.PasswordInput(attrs={"placeholder":'تکرار رمز عبور را وارد کنید'}))
    
    class Meta:
        model=User
        fields=['first_name','last_name','username','password1','password2']
    
    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('رمز عبور با تکرار آن یکسان نیست.')
        return password2

#------------------------------------------------------------------------------------------------------------
class LoginUserForm(forms.Form):
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری را وارد کنید'})
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور را وارد کنید'})
    )
