from django.shortcuts import render
from .models import Services


# Create your views here.

def ServiceView(request):
    service = Services.objects.all()
    context = {
        "services": service
    }

    return render(request, "Files/service_partial.html", context)