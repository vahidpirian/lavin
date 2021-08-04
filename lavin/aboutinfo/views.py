from django.shortcuts import render
from .models import ABOUT_US


def ABOUT_US_VIEW(request):
    about_us = ABOUT_US.objects.first()
    context = {
        'about_us': about_us
    }

    return render(request, "about-us.html", context)