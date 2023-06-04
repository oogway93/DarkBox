from laptops.models import Laptop
from rest_framework import serializers


class LaptopSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = Laptop
        fields = '__all__'
