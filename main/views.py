from django.shortcuts import render, redirect, get_object_or_404
from .models import Orders
from .forms import BForm, NForm, VForm, Filt
from django.views.generic import UpdateView
import re


class BUpdateView(UpdateView):
    model = Orders
    template_name = 'main/beznal.html'
    form_class = BForm


class NUpdateView(UpdateView):
    model = Orders
    template_name = 'main/nal.html'
    form_class = NForm


class VUpdateView(UpdateView):
    model = Orders
    template_name = 'main/vozv.html'
    form_class = VForm


def index(request):
    return render(request, 'main/index.html')


def beznal(request):
    error = ''
    if request.method == 'POST':
        form = BForm(request.POST)
        s = request.POST.get("oitems")
        ss = re.findall(r"[\w']+", s)
        n = len(ss)
        fullprice = 0
        for i in range(n//3):
            count = int(ss[i*3 + 1])
            prise = int(ss[i*3 + 2])
            summ = count * prise
            fullprice += summ
        request.POST._mutable = True
        request.POST["osumm"] = str(fullprice)
        request.POST["otype"] = "Безналичная оплата"
        request.POST["oreason"] = '-'
        request.POST["onumb"] = '-'
        request.POST["ovozd"] = '-'
        request.POST["ovozn"] = '-'
        if form.is_valid():
            form.save()
        else:
            error = 'Неверные данные'

    form = BForm()
    data = {'form': form, 'error': error}

    return render(request, 'main/beznal.html', data)


def nal(request):
    error = ''
    if request.method == 'POST':
        form = NForm(request.POST)
        s = request.POST.get("oitems")
        ss = re.findall(r"[\w']+", s)
        n = len(ss)
        fullprice = 0
        for i in range(n // 3):
            count = int(ss[i * 3 + 1])
            prise = int(ss[i * 3 + 2])
            summ = count * prise
            fullprice += summ
        request.POST._mutable = True
        request.POST["osumm"] = str(fullprice)
        request.POST["otype"] = "Оплата наличными"
        if form.is_valid():
            form.save()
            # return redirect('jorn')
        else:
            error = 'Неверные данные'

    form = NForm()
    data = {'form': form, 'error': error}
    return render(request, 'main/nal.html', data)


def vozv(request):
    error = ''
    if request.method == 'POST':
        form = VForm(request.POST)
        s = request.POST.get("oitems")
        ss = re.findall(r"[\w']+", s)
        n = len(ss)
        fullprice = 0
        for i in range(n // 3):
            count = int(ss[i * 3 + 1])
            prise = int(ss[i * 3 + 2])
            summ = count * prise
            fullprice += summ
        request.POST._mutable = True
        request.POST["osumm"] = str(fullprice)
        request.POST["otype"] = "Возврат товара"
        if form.is_valid():
            form.save()
            # return redirect('jorn')
        else:
            error = 'Неверные данные'

    form = VForm()
    data = {'form': form, 'error': error}
    return render(request, 'main/vozv.html', data)


def jorn(request):
    ords = Orders.objects.order_by('-id')
    return render(request, 'main/jorn.html', {'ords': ords})


def otch(request):
    error = ''
    start = ''
    stop = ''
    typpe = ''
    if request.method == 'POST':
        form = Filt(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            start = form.cleaned_data['start']
            stop = form.cleaned_data['stop']
            typpe = form.cleaned_data['type']
        else:
            error = 'Неверные данные'
    else:
        form = Filt()
    ords = Orders.objects.order_by('-id')
    data = {'form': form, 'error': error, 'ords': ords, 'start': start, 'stop': stop, 'type': typpe}
    return render(request, 'main/otch.html', data)
