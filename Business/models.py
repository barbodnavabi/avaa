from django.db import models
from django.utils.translation import gettext as _
from translated_fields import TranslatedField
from django.urls import reverse
# Create your models here.
class Brands(models.Model):
    title=TranslatedField(models.CharField(max_length=300,verbose_name='نام برند'))
    description=TranslatedField(models.TextField(verbose_name='توضیحات',blank=True,null=True))
    image=models.ImageField(upload_to='brands',verbose_name='تصویر یا لوگو برند',blank=True,null=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name='برند'
        verbose_name_plural='برند ها'


class Agents(models.Model):
    company =TranslatedField( models.CharField(max_length=300, verbose_name='نام شرکت'))
    name=TranslatedField(models.CharField(max_length=300,verbose_name='نام نماینده'))
    phone = models.CharField(max_length=300, verbose_name='شماره تلفن',blank=True,null=True)
    description=TranslatedField(models.TextField(verbose_name='توضیحات',blank=True,null=True))
    image=models.ImageField(upload_to='agents',verbose_name='تصویر نماینده',blank=True,null=True)
    State=TranslatedField(models.CharField(max_length=300,verbose_name='نام استان'))
    email=models.EmailField(_("email"), max_length=254,blank=True,null=True)
    timeadd=models.DateTimeField(("timeadd"), auto_now_add=True)


    def __str__(self):
        return self.State


    class Meta:
        verbose_name='نماینده'
        verbose_name_plural='نمایندگان'

    def get_absolute_url(self):
        return reverse("agent-detail", kwargs={"pk": self.pk})
        