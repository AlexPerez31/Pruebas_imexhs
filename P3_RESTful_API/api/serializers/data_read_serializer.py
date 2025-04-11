from rest_framework import serializers
from api.models import ResultEntry

class DataReadSerializer(serializers.ModelSerializer):
    """
    Realice este serializer para representar los datos cuando se hace un GET.
    """
    device_name = serializers.CharField(source='device.device_name')

    class Meta:
        model = ResultEntry
        fields = [
            'id',
            'device_name',
            'average_before_normalization',
            'average_after_normalization',
            'data_size',
            'created_date',
            'updated_date'
        ]