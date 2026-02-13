from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views # Para obtener tokens

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('temperatures.urls')), # Prefijo /api/
    # Ruta para que los usuarios obtengan su token enviando usuario/contraseña
    path('api-token-auth/', views.obtain_auth_token), 
]