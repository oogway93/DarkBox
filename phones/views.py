from django.shortcuts import render

from phones.models import Phone, Manufacturer


def AvailableCatalog(request):
    phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, 'phones/Catalog.html', context)


def Base(request):
    mm = Phone.objects.get('manufacturer')
    context = {'mm': mm}
    return render(request, 'phones/Base.html', context)
