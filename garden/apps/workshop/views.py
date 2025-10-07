from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *


class index(ListView):
    model = Workshop
    template_name = 'workshop/index.html'
    context_object_name = 'workshops'
    queryset = Workshop.objects.order_by('-is_active')
    paginate_by=3

def show_report_text(request,id):
    context={}
    workshop=Workshop.objects.get(id=id)
    workshop.view_number+=1
    workshop.save()
    context['workshop']=workshop
    if WorkshopGallery.objects.filter(workshop_id=id):
        gallery=WorkshopGallery.objects.filter(workshop_id=id)
        context['gallery']=gallery
    else:
        context['message']='هیچ عکسی وجود ندارد'
    return render(request,'workshop/report_text.html',context)