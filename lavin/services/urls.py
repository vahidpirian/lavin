from django.urls import path
from .views import ServiceView

urlpatterns = [
    path('service_partial', ServiceView, name="service_partial")
]
