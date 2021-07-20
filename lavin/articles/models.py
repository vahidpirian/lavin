from django.db import models
from Category.models import Category


# Create your models here.
class ArticleManager(models.Manager):
    def get_active_articles(self):
        return self.get_queryset().filter(active=True)

    def get_articles_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name)

    def get_by_id(self, article_id):
        qs = self.get_queryset().filter(id=article_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(max_length=1000000, verbose_name="توضیحات")
    image = models.FileField(upload_to="Articles/", null=True, blank=True, verbose_name="تصاویر")
    active = models.BooleanField(default=False, verbose_name="فعال/غیرفعال")
    featured = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, blank=True, verbose_name="دسته بندی ها")

    objects = ArticleManager()

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title
