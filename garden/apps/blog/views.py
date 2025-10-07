from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,HttpResponseNotFound

def index(request):
    article_list = Article.objects.prefetch_related('author').all()
    paginator = Paginator(article_list, 3)  # تعداد مقالات در هر صفحه
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj
    }
    return render(request, 'blog/index.html', context)


def more_blog(request,slug,code):
    context={}
    blog=Article.objects.get(slug=slug)
    context['blog']=blog
    blog.visit+=1
    blog.save()
    if ArticleGallery.objects.filter(article_id=code):
        gallery=ArticleGallery.objects.filter(article_id=code)
        context['gallery']=gallery
    else:
        context['message']='هیچ عکسی وجود ندارد'
    return render(request,'blog/more_blog.html',context)


def show_pdf(request,file_name):
    fs=FileSystemStorage()
    file_name2='pdf/'+str(file_name)
    if fs.exists(file_name2):
        with fs.open(file_name2) as pdf:
            response=HttpResponse(pdf,content_type='application/pdf')
            response['content-Disposition']=f'attachment; filename={file_name}'
            return response
    else:
        return HttpResponseNotFound('File Not Found...')
    