from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_yasg.utils import swagger_auto_schema
from .models import CityTemperature
from .serializers import CityTemperatureSerializer

class CityTemperatureViewSet(viewsets.ModelViewSet):
    """
    Vista principal para gestionar las temperaturas de las ciudades.
    """
    queryset = CityTemperature.objects.all()
    serializer_class = CityTemperatureSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

@swagger_auto_schema(operation_description="Lista todas las ciudades registradas y sus temperaturas. No requiere token.")
def list(self, request, *args, **kwargs):
    return super().list(request, *args, **kwargs)

@swagger_auto_schema(operation_description="Crea un nuevo registro de temperatura. Requiere enviar un Token de autenticación en los Headers.")
def create(self, request, *args, **kwargs):
    return super().create(request, *args, **kwargs)