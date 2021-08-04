from django.urls import path
from .views import lavinbanner

urlpatterns = [
    path('banner_partial', lavinbanner.as_view(), name="banner_partial")
]