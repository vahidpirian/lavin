from django.urls import path
from .views import GalleryListView, Gallery_Category, GalleryListByCategory, Gallery_List_partial

urlpatterns = [
    path("gallery", GalleryListView.as_view()),
    path('gallery/<gallery_name>', GalleryListByCategory.as_view()),
    path('gallery_category_partial', Gallery_Category, name="gallery_category_partial"),
    path('gallery_list_partial', Gallery_List_partial, name="gallery_list_partial")
]