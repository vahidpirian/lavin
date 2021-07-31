from django.db import models


# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=20, verbose_name="عنوان")
    image = models.FileField(upload_to="Services/", null=True, blank=True, verbose_name="عکس")
    url = models.CharField(max_length=100, verbose_name="آدرس", null=True)

    class Meta:
        verbose_name = "خدمات"
        verbose_name_plural = "خدمات"

    def __str__(self):
        return self.title
