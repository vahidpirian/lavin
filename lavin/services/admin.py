from django.contrib import admin
from .models import Services


# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ("__str__", "image")

    class Meta:
        model = Services


admin.site.register(Services, ServiceAdmin)
