import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import ResultEntry
from api.serializers.data_update_serializer import DataUpdateSerializer

# Configuré el logger para esta vista
logger = logging.getLogger(__name__)

class DataUpdateView(APIView):
    """
    Esta vista permite hacer un PUT para actualizar el ID o el nombre de un dispositivo
    """

    def put(self, request, pk):
        logger.info(f"Inicié solicitud PUT para actualizar la entrada con ID actual: {pk}")

        try:
            # Busqué el registro que corresponde al ID pasado en la URL
            instance = ResultEntry.objects.get(pk=pk)
        except ResultEntry.DoesNotExist:
            logger.warning(f"No se encontró ninguna entrada con ID: {pk}")
            return Response({"error": "No existe una entrada con este ID."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DataUpdateSerializer(instance, data=request.data)

        # Aca quise verificar si los nuevos datos son válidos
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Entrada actualizada correctamente. Nuevo estado: {serializer.data}")
            return Response({"message": "Entrada actualizada correctamente."}, status=status.HTTP_200_OK)
        else:
            logger.warning(f"Errores de validación al actualizar ID {pk}: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
