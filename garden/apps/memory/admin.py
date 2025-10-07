from django.contrib import admin
from .models import *


@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display=('title','user','register_date','status')
    ordering=['status','register_date']
    
@admin.register(MemoryGallery)
class MemoryGalleryAdmin(admin.ModelAdmin):
    list_display=('memory',)
    ordering=['memory']
 
@admin.register(MemoryLike)   
class MemoryLikeAdmin(admin.ModelAdmin):
    list_display=('user','memory')
    ordering=['memory']