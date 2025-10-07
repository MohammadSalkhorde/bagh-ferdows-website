from django.contrib import admin
from .models import *

@admin.register(WorkshopStatus)
class WorkshopStatusAdmin(admin.ModelAdmin):
    list_display=('status_code','status_title',)
    ordering=['status_code',]

@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display=('title','place','teacher','register_date','is_active',)
    ordering=['is_active','register_date']

@admin.register(WorkshopGallery)
class WorkshopGalleryAdmin(admin.ModelAdmin):
    list_display=('workshop',)
    ordering=['workshop']