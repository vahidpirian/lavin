from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'image']

    class Meta:
        model = Article


admin.site.register(Article, ArticleAdmin)
