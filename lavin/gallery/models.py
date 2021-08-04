from django.db import models
from Category.models import Category


# Create your models here.

class GalleryManager(models.Manager):
    def get_gallery_by_category(self, gallery_name):
        return self.get_queryset().filter(categories__name__iexact=gallery_name)


class Gallery(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(max_length=1000, verbose_name="توضیحات")
    image = models.FileField(upload_to="Galleries/", verbose_name="تصاویر")
    categories = models.ManyToManyField(Category, verbose_name="دسته بندی ها")

    objects = GalleryManager()

    class Meta:
        verbose_name = "گالری"
        verbose_name_plural = "گالری"

    def __str__(self):
        return self.title
