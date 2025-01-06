from django.db import models


class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.TextField()

    def __str__(self):
        return f"Data received at {self.timestamp}"
