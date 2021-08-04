import itertools
from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import ListView
# Create your views here.
from .models import Article
from Category.models import Category


def grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


class ArticleListView(ListView):
    template_name = "articles/article_list.html"
    paginate_by = 12

    def get_context_data(self, *args, object_list=None, **kwargs):
        latest_articles = Article.objects.order_by('-id').all()[:4]
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        context['latest_articles'] = grouper(4, latest_articles)
        return context

    def get_queryset(self):
        return Article.objects.all()


class ArticleListByCategory(ListView):
    template_name = "articles/article_list.html"
    paginate_by = 12

    def get_context_data(self, *args, object_list=None, **kwargs):
        latest_articles = Article.objects.order_by('-id').all()[:4]
        context = super(ArticleListByCategory, self).get_context_data(*args, **kwargs)
        context['latest_articles'] = grouper(4, latest_articles)
        return context

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category = Category.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404("صفحه مورد نظر یافت نشد")
        return Article.objects.get_articles_by_category(category_name)


def ArticleDetailView(requset, **kwargs):
    article_id = kwargs['articleId']
    # article_name = kwargs['name']
    article = Article.objects.get_by_id(article_id)
    related_articles = Article.objects.get_queryset().filter(categories__article=article)
    grouped_articles = grouper(4, related_articles)
    latest_articles = Article.objects.order_by('-id').all()[:4]
    # date_time = Article.objects.jalali_date_time(date)
    if article is None:
        raise Http404("موجود نیست")
    context = {
        'article': article,
        'related_articles': grouped_articles,
        'latest_articles': grouper(4, latest_articles)
    }
    return render(requset, "articles/article_detail.html", context)


def Article_Category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, "articles/article_categories_partial.html", context)


class SearchArticles(ListView):
    template_name = "articles/article_list.html"
    paginate_by = 12

    def get_context_data(self, *args, object_list=None, **kwargs):
        latest_articles = Article.objects.order_by('-id').all()[:4]
        context = super(SearchArticles, self).get_context_data(*args, **kwargs)
        context['latest_articles'] = grouper(4, latest_articles)
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Article.objects.search(query)
        return Article.objects.none()


def Article_Footer_partial(request):
    latest_article = Article.objects.order_by('id').all()[:4]
    context = {
        'latest_article': grouper(4, latest_article)
    }
    return render(request, "articles/article_footer_partial.html", context)