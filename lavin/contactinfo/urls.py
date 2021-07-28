from django.urls import path
from .views import Contact_Form

urlpatterns = [
    path('contact-us', Contact_Form)
]