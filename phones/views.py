from django.shortcuts import render

from phones.models import Phone


def AvailableCatalog(request):
    phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, 'phones/Catalog.html', context)
