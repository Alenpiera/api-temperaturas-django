from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import CityTemperature

class TemperatureTests(APITestCase):
    def setUp(self):
        # Datos iniciales
        self.user = User.objects.create_user(username='testuser', password='123')
        self.city_data = {'city': 'Caracas', 'temperature': 28.5}
        self.url = reverse('citytemperature-list') # Busca la URL automáticamente

    def test_get_temperatures_public(self):
        """Cualquiera debe poder ver las temperaturas (GET)"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_temperature_unauthenticated(self):
        """Sin loguearse, NO se debe poder crear (POST) -> Espera 401"""
        response = self.client.post(self.url, self.city_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_temperature_authenticated(self):
        """Logueado, SÍ se debe poder crear (POST) -> Espera 201"""
        self.client.force_authenticate(user=self.user) # Simulamos login
        response = self.client.post(self.url, self.city_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CityTemperature.objects.count(), 1)