from django.db import models


# Create your models here.

class ADV(models.Model):
    video = models.FileField(upload_to="adv_files", null=True, blank=True, verbose_name="فیلم تبلیغاتی")

    class Meta:
        verbose_name = "تبلیغ"
        verbose_name_plural = "تبلیغات"

    def __str__(self):
        return str.title
