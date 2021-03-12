from django.db import models


class Contactus(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    subject = models.CharField(max_length=200, verbose_name='عنوان پیام')
    phone = models.CharField(max_length=200,blank=True, verbose_name='تلفن')
    text = models.TextField(verbose_name='متن پیام')
    is_read = models.BooleanField(default=False,verbose_name='خوانده شده / نشده')
    datetime= models.DateTimeField(("datetime"), auto_now_add=True)

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس های کاربران'

    def __str__(self):
        return self.subject


    def get_absolute_url(self):
       return "/"