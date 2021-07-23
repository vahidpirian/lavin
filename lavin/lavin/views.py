import itertools
from django.shortcuts import render
from django.views.generic import ListView
from articles.models import Article
from banner.models import LavinBanner
from gallery.models import Gallery
# from adv.models import ADV


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
    return render(request, "home.html", context)


def About_Us(request):
    return render(request, "about-us.html", {})


def Gallery_List_partial(request):
    gallery_list = Gallery.objects.all()
    latest_gallery = Gallery.objects.order_by('-id').all()[:4]
    context = {
        'gallery_list': gallery_list,
        'latest_gallery': grouper(4, latest_gallery)
    }
    return render(request, "Shared/Gallery_List_partial.html", context)


def Article_List_partial(request):
    latest_article = Article.objects.order_by('id').all()[:4]
    context = {
        'latest_article': grouper(4, latest_article)
    }
    return render(request, "Shared/Footer_Partial.html", context)


# def adv(request):
#     adv_home = ADV.objects.all()
#     context = {
#         'adv_home': adv_home
#     }
#
#     return render(request, 'adv.html', context)