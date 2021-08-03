from django.db import models


# Create your models here.

class LavinBanner(models.Model):
    objects = None
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    links = models.CharField(max_length=500, verbose_name='لینک')
    image = models.FileField(upload_to="banner/", verbose_name="تصویر")

    class Meta:
        verbose_name = "بنر"
        verbose_name_plural = "بنر"

    def __str__(self):
        return self.title
