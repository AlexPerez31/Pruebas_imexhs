import logging
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.data_upload_serializer import DataSerializer

# Configuré el logger para esta vista
logger = logging.getLogger(__name__)


class DataUploadView(APIView):
    """
    Esta vista hace un POST para cargar los datos que recibe del JSON
    """

    def post(self, request):
        success_ids = []
        errors = {}

        logger.info("Inicié procesamiento del JSON recibido en POST.")

        for key, data_block in request.data.items():
            logger.info(f"Procesando entrada con clave: {key} y ID: {data_block.get('id', 'N/A')}")

            # A cada bloque le apliqué el DataSerializer que ya había definido
            serializer = DataSerializer(data=data_block)

            # Verifiqué si los datos eran válidos
            if serializer.is_valid():
                try:
                    serializer.save()
                    logger.info(f"Entrada válida. Guardé en base de datos con ID: {data_block['id']}")
                    success_ids.append(data_block["id"])
                except IntegrityError:
                    logger.error(f"Ya existe una entrada con ID duplicado: {data_block['id']}")
                    errors[key] = {"id": ["Esta ID ya existe en la base de datos."]}
            else:
                logger.warning(f"Entrada inválida para clave: {key}. Errores: {serializer.errors}")
                errors[key] = serializer.errors

        if errors:
            logger.warning(f"Finalicé procesamiento con errores en {len(errors)} entradas.")
            return Response({
                "message": "Se procesaron algunas entradas, pero otras fallaron.",
                "success_ids": success_ids,
                "errors": errors
            }, status=status.HTTP_207_MULTI_STATUS)

        logger.info(f"Finalicé procesamiento. Todas las entradas se guardaron correctamente. Total: {len(success_ids)}")
        return Response({
            "message": "Todas las entradas se procesaron correctamente.",
            "success_ids": success_ids
        }, status=status.HTTP_201_CREATED)