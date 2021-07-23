from django.shortcuts import render
from django.views.generic import ListView
from .models import Contact_Us
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.


class contact_us(ListView):
    template_name = "contact-us.html"

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(contact_us, self).get_context_data(*args, **kwargs)
        context["form"] = ContactForm
        return context

    def get_queryset(self):
        return Contact_Us.objects.first()


def WhatsAppData(phone, message, name):
    import time
    import webbrowser as web
    import pyautogui as pg
    phone = "+98" + phone
    web.open("https://web.whatsapp.com/send?=" + phone + "&text=" + message + "&name" + name)
    time.sleep(30)
    pg.press("enter")

    def SendData(request):
        if request.method == "POST":
            Name = request.POST['FullName']
            ph = request.POST['Phone']
            Message = request.POST['Text']
            WhatsAppData(ph, Message, Name)
            msg = "پیغام با موفقیت ارسال شد.."
            return render(request, "contact-us.html", {
                "msg": msg
            })
        else:
            return HttpResponse("<h1>404 - Not Found :)</h1>")
