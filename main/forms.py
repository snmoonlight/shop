from .models import Orders
from django.forms import ModelForm, TextInput, Form
from django import forms


class BForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['otype', 'odate', 'oname', 'oitems', 'osumm']

        widgets = {
            "otype": TextInput(attrs={'class': 'form-control', 'placeholder': 'Вид продажи'}),
            "odate": TextInput(attrs={'class': 'form-control', 'placeholder': 'Дата продажи'}),
            "oname": TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя покупателя'}),
            "oitems": TextInput(attrs={'class': 'form-control', 'placeholder': 'Товары'}),
            "osumm": TextInput(attrs={'class': 'form-control', 'placeholder': 'Общая сумма'}),
        }


class NForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['otype', 'odate', 'onumb', 'oitems', 'osumm']

        widgets = {
            "otype": TextInput(attrs={'class': 'form-control', 'placeholder': 'Вид продажи'}),
            "odate": TextInput(attrs={'class': 'form-control', 'placeholder': 'Дата продажи'}),
            "onumb": TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер кассового аппарата'}),
            "oitems": TextInput(attrs={'class': 'form-control', 'placeholder': 'Товары'}),
            "osumm": TextInput(attrs={'class': 'form-control', 'placeholder': 'Общая сумма'})
        }


class VForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['otype', 'odate', 'oname', 'oitems', 'osumm', 'oreason', 'ovozd', 'ovozn']

        widgets = {
            "otype": TextInput(attrs={'class': 'form-control', 'placeholder': 'Вид продажи'}),
            "odate": TextInput(attrs={'class': 'form-control', 'placeholder': 'Дата продажи'}),
            "oname": TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя клиента'}),
            "oitems": TextInput(attrs={'class': 'form-control', 'placeholder': 'Товары'}),
            "osumm": TextInput(attrs={'class': 'form-control', 'placeholder': 'Общая сумма'}),
            "oreason": TextInput(attrs={'class': 'form-control', 'placeholder': 'Причина возврата'}),
            "ovozd": TextInput(attrs={'class': 'form-control', 'placeholder': 'Дата документа продажи'}),
            "ovozn": TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер документа продажи'})
        }


class Filt(forms.Form):
    start = forms.DateField(required=False)
    stop = forms.DateField(required=False)
    type = forms.CharField(max_length=100, required=False)