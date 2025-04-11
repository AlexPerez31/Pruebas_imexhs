from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import ResultEntry
from api.serializers.data_read_serializer import DataReadSerializer
from django.utils.dateparse import parse_datetime
from django.db.models import Q
import logging

# Configuré el logger para esta vista
logger = logging.getLogger(__name__)

class DataListView(APIView):
    """
    Esta vista permite hacer un GET para listar los registros con o sin filtros.
    """

    def get(self, request):
        logger.info("Inicié la consulta de datos con filtros opcionales.")
        queryset = ResultEntry.objects.all()

        # Estos los que identifique como los filtros numéricos y de fechas que soportan operadores
        filter_fields = [
            'created_date',
            'updated_date',
            'average_before_normalization',
            'average_after_normalization',
            'data_size'
        ]

        # Recorro cada filtro y parametro para verificar si fue pasado en la URL
        for field in filter_fields:
            for operator in ['exact', 'gt', 'gte', 'lt', 'lte']:
                param = f"{field}__{operator}"
                value = request.query_params.get(param)
                # Verifico si se paso un filtro
                if value:
                    # Esta logica la hice especifica para la fecha
                    if 'date' in field:
                        value = parse_datetime(value)
                        if value is None:
                            logger.warning(f"Fecha inválida para filtro: {param}")
                            continue
                    try:
                        queryset = queryset.filter(**{param: value})
                        logger.info(f"Apliqué filtro: {param}={value}")
                    except Exception as e:
                        logger.error(f"Error al aplicar filtro {param}: {e}")

        serializer = DataReadSerializer(queryset, many=True)
        logger.info(f"Finalicé la consulta. Total de registros encontrados: {len(serializer.data)}")
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class DataDetailView(APIView):
    """
    Esta vista hace un GET para obtener un registro específico según su ID.
    """

    def get(self, request, pk):
        # Primero intenté buscar el objeto con la ID proporcionada en la url
        try:
            result = ResultEntry.objects.get(pk=pk)
            logger.info(f"Consulta exitosa para ID: {pk}")
        except ResultEntry.DoesNotExist:
            logger.warning(f"No encontré ningún registro con ID: {pk}")
            return Response(
                {"error": f"No se encontró ningún registro con el ID: {pk}"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Serialicé y devolví los datos si todo salió bien
        serializer = DataReadSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)