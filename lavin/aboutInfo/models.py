from django.db import models


# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    image = models.FileField(upload_to="about-us-image", blank=True, null=True, verbose_name="عکس")

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"

    def __str__(self):
        return self.title
