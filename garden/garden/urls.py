from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.mainApp.urls',namespace='main')),
    path('garden/',include('apps.introduction.urls',namespace='garden')),
    path('blog/',include('apps.blog.urls',namespace='blog')),
    path('workshop/',include('apps.workshop.urls',namespace='workshop')),
    path('account/',include('apps.accounts.urls',namespace='account')),
    path('memory/',include('apps.memory.urls',namespace='memory')),
    path('search/',include('apps.search.urls',namespace='search')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
