from django.db import models


class ABOUT_DR(models.Model):
    title = models.CharField(max_length=120, verbose_name="عنوان")
    description = models.TextField(max_length=10000, verbose_name="توضیحات")
    image = models.FileField(upload_to="about_dr", verbose_name="عکس")
    address = models.CharField(max_length=500, verbose_name="آدرس")

    class Meta:
        verbose_name = "درباره دکتر"
        verbose_name_plural = "ماژول درباره دکتر"

    def __str__(self):
        return self.title
