from rest_framework import serializers
from .models import Device

# Serializing the models

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('device','location','mode')