from rest_framework import serializers
from ..models import ResultEntry, Device

class DataUpdateSerializer(serializers.Serializer):
    """
    Este serializer lo creé para actualizar el ID o el nombre del dispositivo de un registro
    """

    id = serializers.CharField(required=False)
    device_name = serializers.CharField(required=False)

    def update(self, instance, validated_data):
        if 'id' in validated_data:
            instance.id = validated_data['id']

        if 'device_name' in validated_data:
            device, _ = Device.objects.get_or_create(device_name=validated_data['device_name'])
            instance.device = device

        instance.save()
        return instance
