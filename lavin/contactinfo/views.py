from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from .models import Contact_Us, ContactFormModel
from .forms import ContactForm


def Contact_Form(request):
    form = ContactForm(request.POST or None)
    object_list = Contact_Us.objects.first()
    context = {
        'form': form,
        'object_list': object_list
    }
    if form.is_valid():
        fullName = form.cleaned_data.get('FullName')
        phone = form.cleaned_data.get('Phone')
        text = form.cleaned_data.get('Text')
        Data = ContactFormModel(FullName=fullName, Phone=phone, Text=text)
        Data.save()
        context['form'] = ContactForm

    return render(request, 'contact-us.html', context)


def Contact_Partial(request):
    contact = Contact_Us.objects.first()
    context = {
        'contact': contact
    }

    return render(request, 'contact_partial.html', context)
# def WhatsAppData(phone, message, name):
#     import time
#     import webbrowser as web
#     import pyautogui as pg
#     phone = "+98" + phone
#     web.open("https://web.whatsapp.com/send?=" + phone + "&text=" + message + "&name" + name)
#     time.sleep(30)
#     pg.press("enter")
#
#     def SendData(request):
#         if request.method == "POST":
#             Name = request.POST['FullName']
#             ph = request.POST['Phone']
#             Message = request.POST['Text']
#             WhatsAppData(ph, Message, Name)
#             msg = "پیغام با موفقیت ارسال شد.."
#             return render(request, "contact-us.html", {
#                 "msg": msg
#             })
#         else:
#             return HttpResponse("<h1>404 - Not Found :)</h1>")
