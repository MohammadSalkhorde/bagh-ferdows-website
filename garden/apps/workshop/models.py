from django.db import models
from django.utils import timezone

class WorkshopStatus(models.Model):
    status_code=models.IntegerField(verbose_name='کد وضعیت',primary_key=True)
    status_title=models.CharField(verbose_name='عنوان وضعیت',max_length=50)
    
    def __str__(self) -> str:
        return self.status_title
    
    class Meta:
        verbose_name='وضعیت کارگاه'
        verbose_name_plural="وضعیت کارگاه ها"
        
        
def upload_workshop_image(instance,photo_name):
    return f'images/workshop/{photo_name}'
class Workshop(models.Model):
    title=models.CharField(verbose_name='عنوان کارگاه',max_length=100)
    photo=models.ImageField(verbose_name='تصویر اصلی',upload_to=upload_workshop_image)
    date=models.DateTimeField(verbose_name='تاریخ و زمان برگزاری')
    place=models.CharField(verbose_name='مکان برگزاری',max_length=50)
    teacher=models.CharField(verbose_name='مدرس',max_length=80)
    information=models.TextField(verbose_name='اطلاعات')
    registeration=models.TextField(verbose_name='شرایط ثبت نام')
    report_text=models.TextField(verbose_name='متن گزارش',null=True,blank=True)
    view_number=models.IntegerField(verbose_name='تعداد بازدید',default=0)
    register_date=models.DateTimeField(verbose_name='تاریخ ثبت',default=timezone.now)
    is_active=models.BooleanField(verbose_name='وضعیت فعال / غیر فعال',default=False)
    status=models.ForeignKey(WorkshopStatus,on_delete=models.CASCADE,verbose_name='وضعیت کارگاه')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name='کارگاه'
        verbose_name_plural="کارگاه ها"
        
def upload_gallery_image(instance,photo_name):
    return f'images/workshop/gallery/{instance.workshop.id}/{photo_name}'
class WorkshopGallery(models.Model):
    workshop=models.ForeignKey(Workshop,on_delete=models.CASCADE,verbose_name='کارگاه')
    photo=models.ImageField(verbose_name='تصویر',upload_to=upload_gallery_image)
    
    def __str__(self) -> str:
        return f'{self.workshop}'
    
    class Meta:
        verbose_name='تصویر کارگاه'
        verbose_name_plural="تصاویر کارگاه ها"