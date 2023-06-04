from django.shortcuts import render
from django.core.paginator import Paginator

from phones.models import Phone


def CatalogPhone(request):
    phones = Phone.objects.all()
    paginator = Paginator(phones, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'phones': phones, 'page_obj': page_obj}
    return render(request, 'phones/Catalog_Phone.html', context)


def Base(request):
    return render(request, 'base.html')