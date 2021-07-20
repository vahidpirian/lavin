from django.contrib import admin

# Register your models here.
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'image', 'active']

    class Meta:
        model = Article


admin.site.register(Article, ArticleAdmin)
