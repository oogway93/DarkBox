from django.shortcuts import render

from laptops.models import Laptop


def CatalogLaptop(request):
    laptops = Laptop.objects.all()
    context = {'laptops': laptops}
    return render(request, 'laptops/Catalog_Laptop.html', context)
