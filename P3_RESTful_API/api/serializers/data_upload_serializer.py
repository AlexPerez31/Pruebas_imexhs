from rest_framework import serializers
from ..models import Device, ResultEntry

class DataSerializer(serializers.Serializer):
    """
    Realice este serializer para validar y transformar cada entrada individual del JSON.
    """
    # Primero definí los campos básicos que segun la información se esperan en cada entrada
    id = serializers.CharField()
    data = serializers.ListField(child=serializers.CharField())
    deviceName = serializers.CharField()


    def validate(self, data):
        """
        Esta función valida todo lo que llega en el campo data,
        convierte los strings en números, calcula promedios y normaliza.
        """
        raw_numbers = []

        for line in data['data']:
            try:
                # Dividí el string en partes, conviertí cada parte a float y lo agregué a la lista
                raw_numbers.extend([float(x) for x in line.strip().split()])
            except ValueError:
                raise serializers.ValidationError("Todos los valores en el campo data deben ser números válidos.")

        if not raw_numbers:
            raise serializers.ValidationError("La lista 'data' está vacía o no contiene números válidos.")

        # Aca comienzo a hacer cada uno de los calculos requerridos usando funciones de python
        max_val = max(raw_numbers)
        if max_val == 0:
            raise serializers.ValidationError("No se puede normalizar si el valor máximo es 0.")

        # Promedio antes de normalizar
        avg_before = sum(raw_numbers) / len(raw_numbers)

        # Normalizo todos los datos dividiendo cada uno entre el valor máximo
        normalized = [x / max_val for x in raw_numbers]

        # Calculo el promedio después de normalizar
        avg_after = sum(normalized) / len(normalized)

        data['flat_data'] = raw_numbers
        data['normalized_data'] = normalized
        data['average_before'] = round(avg_before, 4)
        data['average_after'] = round(avg_after, 4)
        data['data_size'] = len(raw_numbers)
        return data


    def create(self, validated_data):
        """
        Esta función es para guardar los datos en la base de datos
        Tambien creo el Device si no existe.
        """
        device, _ = Device.objects.get_or_create(device_name=validated_data['deviceName'])

        try:
            return ResultEntry.objects.create(
                id=validated_data['id'],
                device=device,
                data_size=validated_data['data_size'],
                average_before_normalization=validated_data['average_before'],
                average_after_normalization=validated_data['average_after']
            )
        except Exception as e:
            # Si hubo un error, como una id duplicada en los distintos archivos
            raise serializers.ValidationError(f"Error al guardar en la base de datos: {str(e)}")