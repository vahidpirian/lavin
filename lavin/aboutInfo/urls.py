from django.urls import path
from .views import AboutUsListView, AboutUsPage
urlpatterns = [
    path('about-us', AboutUsListView.as_view()),
    path('aboutus', AboutUsPage)
]