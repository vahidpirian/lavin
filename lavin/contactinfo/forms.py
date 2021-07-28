from django import forms
from .models import ContactFormModel


class ContactForm(forms.Form):
    FullName = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "نام و نام خانوادگی خود را وارد کنید"
        }), label="نام و نام خانوادگی", max_length=128)

    Phone = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "placeholder": "تلفن تماس را وارد کنید"
        }
    ), label="تلفن", max_length=128)

    Text = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "پیام خود را وارد کنید"
        }
    ), label="متن", max_length=10000)

    class Meta:
        model = ContactFormModel
        fields = ('FullName', 'Phone', 'Text')
