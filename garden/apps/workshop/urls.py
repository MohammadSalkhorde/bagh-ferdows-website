from django.urls import path
from .views import *

app_name='workshop'
urlpatterns = [
    path('',index.as_view(),name='index'),
    path('report_text/<int:id>',show_report_text,name='report_text'),
]