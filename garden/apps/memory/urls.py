from django.urls import path
from .views import *

app_name='memory'
urlpatterns = [
    path('memories/',AllMemory.as_view(),name='index'),
    path('like/',like,name='like'),
    path('removelike/',removelike,name='removelike'),
    path('addmemory/',AddMemory.as_view(),name='addmemory'),
    # path('update/<int:id>/',UpdateMemory.as_view(),name='update'),
]