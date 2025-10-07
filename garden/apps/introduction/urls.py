from django.contrib import admin
from django.urls import path,include,re_path
import apps.introduction.views as views
# from django.conf.urls import url

app_name='garden'
urlpatterns = [
    path('',views.index,name='introducion'),
    path('contact/',views.contact1,name='contact'),
    path('rules/',views.rules,name='rules'),
    path('rules/ticket/',views.ticket,name='ticket'),
    path('pdf/',views.show_pdf,name='pdf'),
    path('history/',views.history,name='history'),
    re_path(r'^place/(?P<title_place>[-\w]{5,10})/$',views.places,name='place'),
]
