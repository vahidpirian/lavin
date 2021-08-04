from django.shortcuts import render
from django.views.generic import ListView

from .models import LavinBanner


# Create your views here.

# def lavinbanner(request):
#     banner = LavinBanner.objects.all()
#     print(banner)
#     context = {
#         'banner': banner
#     }
#     return render(request, "banner_partial.html", context)

class lavinbanner(ListView):
    template_name = "banner_partial.html"

    def get_queryset(self):
        return LavinBanner.objects.all()
