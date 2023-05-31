from django.shortcuts import render

from phones.models import Phone



def CatalogPhone(request):
    phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, 'phones/Catalog_Phone.html', context)

