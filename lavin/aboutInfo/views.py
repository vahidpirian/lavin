from django.shortcuts import render
from django.views.generic import ListView

from .models import AboutUs


# Create your views here.

def AboutUsPage(request):
    about_us = AboutUs.objects.first()
    context = {
        'about-us': about_us
    }

    return render(request, "about-us.html", context)


class AboutUsListView(ListView):
    template_name = "about-us.html"

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(AboutUsListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        return AboutUs.objects.first()
