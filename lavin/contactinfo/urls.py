from django.urls import path
from .views import Contact_Form, Contact_Partial

urlpatterns = [
    path('contact-us', Contact_Form),
    path('contact_footer_partial', Contact_Partial, name='contact_footer_partial')
]