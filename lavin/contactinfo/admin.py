from django.contrib import admin
from .models import Contact_Us
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'description', 'phone', 'address', 'email')

    class Meta:
        model = Contact_Us

admin.site.register(Contact_Us, ContactAdmin)