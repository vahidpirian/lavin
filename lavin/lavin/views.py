import itertools
from django.shortcuts import render
from articles.models import Article
from banner.models import LavinBanner



def grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def Home_Page(request):
    banner = LavinBanner.objects.first()
    latest_articles = Article.objects.order_by('-id').all()[:4]
    context = {
        'latest_articles': grouper(4, latest_articles),
        'banner': banner
    }
    return render(request, "Shared/home.html", context)


def About_Us(request):
    return render(request, "about-us.html", {})