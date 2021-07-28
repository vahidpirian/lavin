from django.urls import path
from .views import ABOUT_US_VIEW

urlpatterns = [
    path('aboutus', ABOUT_US_VIEW)
]