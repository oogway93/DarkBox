from phones.models import Phone
from rest_framework import serializers


class PhoneSerializer(serializers.ModelSerializer):
    pass

    class Meta:
        model = Phone
        fields = '__all__'
