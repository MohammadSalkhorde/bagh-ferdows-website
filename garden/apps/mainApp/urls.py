from django.contrib import admin
from django.urls import path,include
import apps.mainApp.views as views

app_name='main'
urlpatterns = [
    path('',views.index,name='index'),

]
