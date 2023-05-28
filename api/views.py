from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from phones.serializers import PhoneSerializer
from phones.models import Phone


class PhonesModelViewSet(ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    # permission_classes = ['IsAuthenticated']
