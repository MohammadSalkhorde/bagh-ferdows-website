from django.urls import path
from .views import *


app_name='account'
urlpatterns = [
    path('register/',RegisterUserView.as_view(),name='register'),
    path('logout/',LogoutUserView.as_view(),name='logout'),
    path('login/',LoginUserView.as_view(),name='login'),
]
