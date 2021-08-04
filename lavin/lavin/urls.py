from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import Home_Page, About_Us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home_Page),
    path('about-us', About_Us),
    path('', include('contactinfo.urls')),
    path('', include('articles.urls')),
    path('', include('services.urls')),
    path('', include('gallery.urls')),
    path('', include('banner.urls')),
    path('', include('aboutinfo.urls')),
    path('', include('about_dr.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)