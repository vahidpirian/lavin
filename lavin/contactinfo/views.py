from django.shortcuts import render
from django.views.generic import ListView
from .models import Contact_Us
from .forms import ContactForm
# Create your views here.


class contact_us(ListView):
    template_name = "contact-us.html"

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(contact_us, self).get_context_data(*args, **kwargs)
        context["form"] = ContactForm
        return context

    def get_queryset(self):
        return Contact_Us.objects.first()