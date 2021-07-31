import unicodedata
from django.db import models
from django.core.files.storage import FileSystemStorage


class ABOUT_US(models.Model):
    title = models.CharField(max_length=120, verbose_name="عنوان")
    description = models.TextField(max_length=10000, verbose_name="توضیحات")
    image = models.FileField(upload_to="about-us", null=True, blank=True, verbose_name="عکس")

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"

    def __str__(self):
        return self.title


class ASCIIFileSystemStorage(FileSystemStorage):
    def get_valid_name(self, name):
        name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore')
        return super(ASCIIFileSystemStorage, self).get_valid_name(name)
