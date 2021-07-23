from django.urls import path
from .views import ArticleListView, ArticleDetailView, \
    ArticleListByCategory, Article_Category, SearchArticles

urlpatterns = [
    path('articles', ArticleListView.as_view()),
    path('articles/<category_name>', ArticleListByCategory.as_view()),
    path('article/search', SearchArticles.as_view()),
    path('article/<articleId>/<name>', ArticleDetailView),
    path('article_categories_partial', Article_Category, name="articles_categories_partial")
]
