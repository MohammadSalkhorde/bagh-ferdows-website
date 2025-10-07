from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

def uploadimage(instance,filename):
    return f'images/memory/{filename}'
class Memory(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user',verbose_name='کاربر')
    title=models.CharField(max_length=200,verbose_name='عنوان خاطره')
    memory_date=models.DateTimeField(verbose_name='تاریخ خاطره',default=timezone.now)
    text=models.TextField(verbose_name='متن خاطره')
    photo=models.ImageField(verbose_name='تصویر اصلی',upload_to=uploadimage)
    register_date=models.DateTimeField(verbose_name='تاریخ ثبت خاطره',auto_now_add=True)
    status=models.BooleanField(verbose_name='وضعیت',default=False)
    
    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name='خاطره'
        verbose_name_plural="خاطرات"

def uploadimage2(instance,filename):
    return f'images/memory/gallery/{instance.memory.id}/{filename}'
class MemoryGallery(models.Model):
    memory=models.ForeignKey(Memory,on_delete=models.CASCADE,related_name='memory_gallery',verbose_name='خاطره')
    photo=models.ImageField(verbose_name='تصویر',upload_to=uploadimage2)
    
    def __str__(self) -> str:
        return f'{self.memory}'
    
    class Meta:
        verbose_name='تصویر خاطره'
        verbose_name_plural="تصاویر خاطرات"
    
class MemoryLike(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر',related_name='user_like')
    memory=models.ForeignKey(Memory,on_delete=models.CASCADE,verbose_name='خاطره',related_name='memory_like')
    
    def __str__(self) -> str:
        return f'{self.memory}'
    
    class Meta:
        verbose_name='لایک'
        verbose_name_plural="لایک ها"
    