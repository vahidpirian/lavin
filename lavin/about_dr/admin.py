from django.contrib import admin
from .models import ABOUT_DR


class ABOUT_DR_ADMIN(admin.ModelAdmin):
    list_display = ('__str__', 'description', 'image')

    class Meta:
        mode = ABOUT_DR


admin.site.register(ABOUT_DR, ABOUT_DR_ADMIN)
