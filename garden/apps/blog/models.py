from django.db import models
from django.utils import timezone


class Author(models.Model):
    name=models.CharField(max_length=30,verbose_name='نام')
    family=models.CharField(max_length=30,verbose_name='نام خانوادگی')
    education=models.CharField(max_length=50,verbose_name='تحصیلات')
    job=models.CharField(max_length=40,verbose_name='شغل')
    email=models.EmailField(verbose_name='ایمیل',max_length=200)
    slug=models.SlugField(verbose_name='اسلاگ',max_length=100)
    number=models.CharField(verbose_name='شماره موبایل',max_length=11)
    is_active=models.BooleanField(verbose_name='وضعیت',default=False)
    
    def __str__(self) -> str:
        return str(self.name)
    
    class Meta:
        verbose_name='نویسنده'
        verbose_name_plural="نویسنده ها"
    
    
class ArticleGroup(models.Model):
    title=models.CharField(max_length=50,verbose_name='عنوان گروه')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name='گروه مقاله'
        verbose_name_plural="گروه های مقاله"
    
class Article(models.Model):
    article_group=models.ForeignKey(ArticleGroup,on_delete=models.CASCADE,verbose_name='عنوان گروه مقاله')
    title=models.CharField(max_length=1000,verbose_name='عنوان مقاله')
    photo=models.ImageField(verbose_name='تصویر اصلی',upload_to='images/blog/',null=True)
    author=models.ManyToManyField(Author,verbose_name='نویسنده',related_name='articles')
    slug=models.SlugField(verbose_name='اسلاگ',max_length=100)
    short_text=models.CharField(max_length=1000,verbose_name="متن خلاصه")
    text=models.TextField(verbose_name='متن مقاله')
    keywords=models.CharField(verbose_name='کلمات کلیدی',max_length=1000)
    pdf_name=models.CharField(verbose_name='نام فایل پی دی اف مقاله',max_length=200)
    creation_date=models.DateTimeField(verbose_name='تاریخ ثبت مقاله',default=timezone.now)
    publication_date=models.DateTimeField(verbose_name='تاریخ انتشار مقاله',default=timezone.now)
    update_date=models.DateTimeField(verbose_name='تاریخ به روزرسانی مقاله',auto_now=True)
    is_active=models.BooleanField(verbose_name='وضعیت',default=False)
    visit=models.IntegerField(verbose_name='تعداد بازدید',default=0)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name='مقاله'
        verbose_name_plural="مقاله ها"
    
class ArticleGallery(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name='مقاله')
    photo_name=models.ImageField(verbose_name='نام تصویر',upload_to='images/blog/gallery/')
    
    def __str__(self) -> str:
        return f'{self.article}'
    
    class Meta:
        verbose_name='گالری مقاله'
        verbose_name_plural="گالری مقاله ها"