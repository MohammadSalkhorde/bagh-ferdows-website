from django.db import models


class VisitorGroup(models.Model):
    title=models.CharField(verbose_name='عنوان گروه',max_length=50)

    def __str__(self) -> str:
        return f'{self.title}'
    
    class Meta:
        verbose_name='عنوان گروه'
        verbose_name_plural='عنوان گروه ها'
    

class Place(models.Model):
    title=models.CharField(verbose_name='عنوان مکان',max_length=30)
    photo=models.ImageField(upload_to='images/place/',verbose_name='تصویر اصلی')
    visiting_day=models.CharField(max_length=100,verbose_name='روز بازدید')
    visiting_hours=models.CharField(max_length=100,verbose_name='ساعت بازدید')
    rules=models.TextField(verbose_name='قوانین و مقررات')
    more=models.TextField(verbose_name='اطلاعات بیشتر',max_length=3000)
    place_registration_date=models.DateTimeField(verbose_name='تاریخ ثبت مکان',auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name='مکان'
        verbose_name_plural="مکان ها"
    
    
class TicketPrice(models.Model):
    visitor_Group_code=models.ForeignKey(VisitorGroup,verbose_name='گروه بازدید کننده',on_delete=models.CASCADE)
    place_code=models.ForeignKey(Place,verbose_name='مکان بازدید',on_delete=models.CASCADE)
    price=models.IntegerField(verbose_name='قیمت',default=0)

    def __str__(self) -> str:
        return f'{self.price}'

    class Meta:
        verbose_name="بلیت"
        verbose_name_plural="بلیت ها"
    
    

class Message(models.Model):
    full_name=models.CharField(verbose_name='نام و نام خانوادگی',max_length=60)
    email=models.EmailField(verbose_name='آدرس ایمیل')
    title_message=models.CharField(verbose_name='موضوع پیغام',max_length=50)
    text=models.TextField(verbose_name='متن پیغام')
    register_date=models.DateTimeField(verbose_name='تاریخ ثبت پیام',auto_now_add=True)
    is_active=models.BooleanField(verbose_name='وضعیت مشاهده پیغام',default=False)
    
    def __str__(self) -> str:
        return f'{self.full_name} {self.title_message} {self.is_active}'

    class Meta:
        verbose_name="پیغام"
        verbose_name_plural="پیغام ها"
    
    