from django.urls import path
from .views import ABOUT_DR_VIEW

urlpatterns = [
    path('about-dr-partial', ABOUT_DR_VIEW.as_view(), name='about-dr-partial')
]