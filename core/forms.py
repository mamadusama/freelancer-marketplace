from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"placeholder": "Digite Seu Nome"})
    )

    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={"placeholder": "Digite seu E-mail"}),
    )
    phone = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"placeholder": "Digite seu Telefone"}),
    )
    address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={"placehlder": "Digite seu Endereço"}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Digite sua menssagem"})
    )

    def send_email(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        phone = self.cleaned_data["phone"]
        address = self.cleaned_data["address"]
        message = self.cleaned_data["message"]

        send_mail(
            f"Mensagem de {name} <{email}>",
            f"Telefone: {phone}\nEndereço: {address}\n\nMensagem: {message}",
            email,
            [settings.EMAIL_HOST_USER],
        )
