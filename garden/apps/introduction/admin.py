from django.contrib import admin
from .models import VisitorGroup,Place,TicketPrice,Message

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display=('title','place_registration_date')
    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display=('full_name','title_message','is_active','register_date')
    ordering = ['is_active',]
    
@admin.register(TicketPrice)
class TicketPriceAdmin(admin.ModelAdmin):
    list_display=('place_code','visitor_Group_code','price')
    ordering=['visitor_Group_code',]
    
@admin.register(VisitorGroup)
class VisitorGroupAdmin(admin.ModelAdmin):
    list_display=('title',)
