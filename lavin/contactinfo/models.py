from django.db import models


# Create your models here.

class Contact_Us(models.Model):
    title = models.CharField(max_length=30, verbose_name='عنوان')
    description = models.CharField(max_length=500, verbose_name='توضیحات')
    phone = models.CharField(max_length=30, verbose_name='تلفن')
    address = models.CharField(max_length=500, verbose_name="آدرس")
    email = models.EmailField(max_length=50, verbose_name="ایمیل")
    image = models.FileField(upload_to="contact-us", blank=True, null=True, verbose_name="عکس")
    fax = models.CharField(max_length=50, verbose_name="فکس")

    class Meta:
        verbose_name = "تنظیمات تماس با ما"
        verbose_name_plural = "ماژول تنظیمات"

    def __str__(self):
        return self.title