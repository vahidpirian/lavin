from django.shortcuts import render
from .models import ABOUT_DR
from django.views.generic import ListView


class ABOUT_DR_VIEW(ListView):
    template_name = "about_dr_partial.html"

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ABOUT_DR_VIEW, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        return ABOUT_DR.objects.first()
