from django.db import models
import uuid

# Dispositivo medico
class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device_name = models.CharField(max_length=100)

    def __str__(self):
        return self.device_name


# Resultado de la imagen procesada
class ResultEntry(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='results')
    data_size = models.IntegerField()
    average_before_normalization = models.FloatField()
    average_after_normalization = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Entry {self.id} - Device {self.device.device_name}"