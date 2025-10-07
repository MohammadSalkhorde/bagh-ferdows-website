from django.shortcuts import render
from .models import VisitorGroup,Place,Message,TicketPrice
from django.http import HttpResponse,HttpResponseNotFound,JsonResponse
from django.conf import settings
from .forms import contact
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail,EmailMultiAlternatives


# def SendEmail1(subject, message, to):
#     from_email=settings.EMAIL_HOST_USER
#     send_mail(subject,message,from_email,to)

# def SendEmail2(subject, message, html_contect, to):
#     from_email=settings.EMAIL_HOST_USER
#     send=EmailMultiAlternatives(subject,message,from_email,to)
#     send.attach_alternative(html_contect,'text/html')
#     send.send()


def images(request):
    return {'media':settings.MEDIA_URL,}

    
def index(request):
    return render(request,'introduction/introduction.html')


def is_ajax(request):
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

def contact1(request):
    context = {}
    form = contact()
    if request.method == 'POST' and is_ajax(request):
        form = contact(request.POST)
        if form.is_valid():
            try:
                form.save()
                data = form.cleaned_data
                name = data['full_name']
                return JsonResponse({'name': name}, status=200)
            except Exception as e:
                return JsonResponse({'error': 'خطای سرور'}, status=500)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'error': 'خطای نامعتبر بودن فرم'}, status=400)

    context = {'form': form}
    return render(request, 'introduction/contact.html', context)


def rules(request):
    Place1=Place.objects.all()
    
    context={
        "place":Place1,
    }
    return render(request,'introduction/rules.html',context)


def ticket(request):
    Visitor_Group1=VisitorGroup.objects.all()
    Ticket_price1=TicketPrice.objects.all()
    title=Place.objects.all()
    context={
        'ticket':Ticket_price1,
        "group":Visitor_Group1,
    }
    return render(request,'introduction/ticket.html',context)


def show_pdf(request):
    fs=FileSystemStorage()
    file_name='pdf/garden.pdf'
    if fs.exists(file_name):
        with fs.open(file_name) as pdf:
            response=HttpResponse(pdf,content_type='application/pdf')
            response['content-Disposition']='attachment; filename=garden.pdf'
            return response
    else:
        return HttpResponseNotFound('File Not Found...')
    
def history(request):
    return render(request,'introduction/history.html')


def places(request,title_place):
    title_place=title_place.replace('-',' ')
    place=Place.objects.get(title=title_place)
    context={
        'place':place
    }
    return render(request,'introduction/places.html',context)