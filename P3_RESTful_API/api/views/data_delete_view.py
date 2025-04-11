import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import ResultEntry

# Configuré el logger para esta vista
logger = logging.getLogger(__name__)


class DataDeleteView(APIView):
    """
    Esta vista hace un DELETE para eliminar un registro específico por su ID.
    """

    def delete(self, request, pk):
        logger.info(f"Intenté eliminar el registro con ID: {pk}")

        try:
            # Consulté el registro con la ID proporcionada
            entry = ResultEntry.objects.get(id=pk)
            entry.delete()
            logger.info(f"Eliminé exitosamente el registro con ID: {pk}")
            return Response({"message": f"Registro con ID '{pk}' eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
        except ResultEntry.DoesNotExist:
            logger.warning(f"No se encontró ningún registro con ID: {pk}")
            return Response({"error": f"No se encontró ningún registro con ID '{pk}'."}, status=status.HTTP_404_NOT_FOUND)
