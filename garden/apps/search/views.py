from django.shortcuts import render,redirect
from apps.memory.models import Memory
from apps.blog.models import Article
from apps.workshop.models import Workshop
from django.views import View
from django.db.models import Q
class Search(View):
    def get(self,request):
        query=self.request.GET['search']
        if query:
            memories=Memory.objects.filter(
                Q(title__icontains=query)
                
            )
            workshops=Workshop.objects.filter(
                Q(title__icontains=query)
            )
            articles=Article.objects.filter(
                Q(title__icontains=query)

            )
            
            context={
                'memories':memories,
                'workshops':workshops,
                'articles':articles
            }
            return render(request,'search/search.html',context)
        else:
            return redirect('main:index')