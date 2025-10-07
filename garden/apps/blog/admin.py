from django.contrib import admin

from .models import *

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','family','slug','is_active')
    ordering=['is_active',]
    search_fields=('family','name')
    prepopulated_fields={'slug':('name','family')}
    
@admin.register(ArticleGroup)
class ArticleGroupAdmin(admin.ModelAdmin):
    list_display=("title",)
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','article_group','is_active')
    ordering=['is_active',]
    prepopulated_fields={'slug':('title','article_group')}
    
@admin.register(ArticleGallery)
class ArticleGalleryAdmin(admin.ModelAdmin):
    list_display=('article',)
