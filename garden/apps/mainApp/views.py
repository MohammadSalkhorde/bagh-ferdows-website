from django.shortcuts import render
from django.conf import settings


def index(request):
    context={
        'media':settings.MEDIA_URL,
        'image1':'p3.jpg',
    }
    return render(request,'main/index.html',context)