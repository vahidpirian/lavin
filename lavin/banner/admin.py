from django.contrib import admin
from .models import LavinBanner


# Register your models here.


class BannerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'description')

    class Meta:
        model = LavinBanner


admin.site.register(LavinBanner, BannerAdmin)
