from django.contrib import admin
from .models import AboutUs


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("__str__", "description", "image")

    class Meta:
        model = AboutUs


admin.site.register(AboutUs, AboutUsAdmin)