import itertools
from django.shortcuts import render, Http404
from django.views.generic import ListView
from .models import Gallery
from Category.models import Category
from articles.models import Article


def grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


class GalleryListView(ListView):
    template_name = "Files/gallery_list.html"
    paginate_by = 12

    def get_context_data(self, *args, object_list=None, **kwargs):
        latest_article = Article.objects.order_by('-id').all()[:4]
        context = super(GalleryListView, self).get_context_data(*args, **kwargs)
        context['latest_articles'] = grouper(4, latest_article)
        return context

    def get_queryset(self):
        return Gallery.objects.all()


class GalleryListByCategory(ListView):
    template_name = "Files/gallery_list.html"
    paginate_by = 12

    def get_context_data(self, *args, object_list=None, **kwargs):
        latest_article = Article.objects.order_by('-id').all()[:4]
        context = super(GalleryListByCategory, self).get_context_data(*args, **kwargs)
        context['latest_articles'] = grouper(4, latest_article)
        return context

    def get_queryset(self):
        gallery_name = self.kwargs['gallery_name']
        gallery = Category.objects.filter(name__iexact=gallery_name).first()
        if gallery is None:
            raise Http404('صفحه مورد نظر یافت نشد')
        return Gallery.objects.get_gallery_by_category(gallery_name)


def Gallery_List_partial(request):
    gallery_list = Gallery.objects.all()
    latest_gallery = Gallery.objects.order_by('-id').all()[:4]
    context = {
        'gallery_list': gallery_list,
        'latest_gallery': grouper(4, latest_gallery)
    }
    return render(request, "Files/gallery_list_partial.html", context)


def Gallery_Category(request):
    galleries = Category.objects.all()
    context = {
        'galleries': galleries,
    }
    return render(request, "Files/gallery_category_partial.html", context)
