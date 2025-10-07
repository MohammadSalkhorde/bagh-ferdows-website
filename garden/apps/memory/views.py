from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from django.forms import modelformset_factory

class AllMemory(View):
    def get(self,request,*args,**kwargs):
        memories=Memory.objects.filter(status=True)
        if request.user.is_authenticated:
            list_memory_liked=MemoryLike.objects.filter(user=request.user).values('memory')
            list_memory_liked_id=[memory['memory'] for memory in list_memory_liked]
            return render(request,'memory/index.html',{'memories':memories,"list_memory_liked_id":list_memory_liked_id})
        return render(request,'memory/index.html',{"memories":memories})
    
    
def like(request):
    if request.method=='GET':
        memory_id=request.GET['memory']
        memory=Memory.objects.get(id=memory_id)
        liked=MemoryLike.objects.filter(memory=memory_id,user=request.user)
        if not liked:
            liked=MemoryLike(memory=memory)
            liked.user=request.user
            liked.save()
        return HttpResponse('success')
    return HttpResponse('unsuccess')

def removelike(request):
    if request.method=='GET':
        memory_id=request.GET['memory']
        memory=Memory.objects.get(id=memory_id)
        liked=MemoryLike.objects.filter(memory=memory_id,user=request.user)
        if liked:
            liked.delete()
        return HttpResponse('success')
    return HttpResponse('unsuccess')


class AddMemory(View):
    form_set=modelformset_factory(model=MemoryGallery,form=MemoryGalleryForm,extra=4)
    def get(self,request,*args,**kwargs):
        forms=MemoryForm()
        gallery=self.form_set(queryset=MemoryGallery.objects.none())
        return render(request,'memory/add_memory.html',{'form':forms,'gallery':gallery})
    def post(self,request,*args,**kwargs):
        gallery=self.form_set(request.POST,request.FILES)
        forms=MemoryForm(request.POST,request.FILES)
        if forms.is_valid() and gallery.is_valid():
            cd=forms.cleaned_data
            memory=Memory.objects.create(
                user=request.user,
                title=cd['title'],
                text=cd['text'],
                photo=cd['photo'],
                memory_date=cd['memory_date']
            )

            for form in gallery.cleaned_data:
                if form:
                    MemoryGallery.objects.create(
                        photo=form['photo'],
                        memory=memory
                    )
            messages.success(request,'خاطره با موفقیت درج شد.','success')
            return redirect('main:index')
        else:
            messages.error(request,'اطلاعات وارد شده معتبر نمیباشد.','error')
        return render(request,'memory/add_memory.html',{'form':forms,'gallery':gallery})
    
    
    
    

# بخش اپدیت خاطره غیرفعاله


# class UpdateMemory(View):
#     form_set=modelformset_factory(model=MemoryGallery,form=MemoryGalleryForm,extra=4)
#     def get(self,request,id):
#         memory=Memory.objects.get(id=id)
#         form=MemoryForm()
#         gallery=self.form_set(queryset=MemoryGallery.objects.none())
#         return render(request,'memory/update_memory.html',{'form':form,'memory':memory,'gallery':gallery})
    
#     def post(self,request,id):
#         gallery = self.form_set(request.POST, request.FILES)

#         try:
#             title = request.POST['title']
#             text = request.POST['text']
#             photo = request.FILES.get('photo')  
#             memory_date = request.POST.get('memory_date')  

#             memory = Memory.objects.get(id=id)
#             memory.title = title
#             memory.text = text
#             if photo:  
#                 memory.photo = photo
#             if memory_date:
#                 memory.memory_date = memory_date
#             memory.save()

#             if gallery.is_valid():
#                 for photo in gallery.cleaned_data: 
#                     if photo:
#                         MemoryGallery.objects.create(photo=photo['photo'], memory=memory)

#             messages.success(request, 'خاطره با موفقیت اپدیت شد.', 'success')
#             return redirect('main:index')

#         except Exception as e:
#             print(f'Error occurred: {e}')
#             messages.error(request, 'خطا در بروزرسانی خاطره.', 'error')
#             return redirect('main:index')
