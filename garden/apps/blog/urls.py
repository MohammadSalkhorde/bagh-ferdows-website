from django.contrib import admin
from django.urls import path,re_path
from .views import *


app_name='blog'
urlpatterns = [
    path('',index,name='index'),
    # path('more/',more_blog,name='more'),
    re_path(r'^more/(?P<slug>[-\w\d]+)/(?P<code>[\d]+)/$',more_blog,name='more'),
    path('pdf/<str:file_name>/',show_pdf,name='pdf')
    
]
