from django.contrib import admin
from .models import ADV


# Register your models here.

class ADVAdmin(admin.ModelAdmin):
    list_display = ("__str__", "video")

    class Meta:
        model = ADV


admin.site.register(ADV, ADVAdmin)
