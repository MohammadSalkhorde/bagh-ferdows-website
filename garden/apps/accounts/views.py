from django.shortcuts import render,redirect
from .forms import *
from django.views import View
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
#---------------------------------------------------------------------------
class RegisterUserView(View):
    def get(self,request,*args,**kwargs):
        form=RegisterUserForm()
        return render(request,'account/register.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=User(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['username']
            )
            user.set_password(data['password1'])
            user.save()
            login(request,user)
            group = Group.objects.get(name='کاربر عادی')
            group.user_set.add(user)
            messages.success(request,'ثبت نام با موفقیت انجام شد.','success')
            return redirect('main:index')
        else:
            messages.error(request,'اطلاعات وارد شده معتبر نمی باشد.','error')
            return render(request,'account/register.html',{'form':form})
        
#---------------------------------------------------------------------------
class LogoutUserView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        messages.success(request,'با موفقیت از حساب کاربری خود خارج شدید.','success')
        return redirect('main:index')

#---------------------------------------------------------------------------
class LoginUserView(View):
    def get(self, request, *args, **kwargs):
        form = LoginUserForm()
        return render(request, 'account/login.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = LoginUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)

                messages.success(request, 'با موفقیت وارد حساب کاربری خود شدید.', 'success')
                return redirect('main:index')
            else:
                messages.error(request, 'حساب کاربری پیدا نشد.', 'error')
        else:
            messages.error(request, 'اطلاعات وارد شده معتبر نمی‌باشد.', 'error')
        
        return render(request, 'account/login.html', {'form': form})
#---------------------------------------------------------------------------