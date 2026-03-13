from django.db import models

class CityTemperature(models.Model):
    city = models.CharField(max_length=100, unique=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    # auto_now=True actualiza la fecha cada vez que se guarda (Update)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.city}: {self.temperature}°C"