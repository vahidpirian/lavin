from django.contrib import admin
from .models import ABOUT_US


class ABOUT_US_ADMIN(admin.ModelAdmin):
    list_display = ('__str__', 'description', 'image')

    class Meta:
        model = ABOUT_US


admin.site.register(ABOUT_US, ABOUT_US_ADMIN)
