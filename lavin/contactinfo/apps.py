from django.apps import AppConfig


class ContactinfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contactinfo'
    verbose_name = "ماژول تنظیمات"


class ContactFormModel(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ContactFormModel'
    verbose_name = 'ماٰژول کاربران'
