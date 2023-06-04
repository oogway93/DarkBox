from rest_framework.viewsets import ModelViewSet

from laptops.models import Laptop
from laptops.serializers import LaptopSerializer
from phones.serializers import PhoneSerializer
from phones.models import Phone


class PhonesModelViewSet(ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer


class LaptopsModelViewSet(ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
