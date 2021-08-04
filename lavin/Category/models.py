from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    name = models.CharField(max_length=200, verbose_name="عنوان در url")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.title
