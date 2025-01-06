from django.shortcuts import render
from .models import SensorData


def sensor_data_view(request):
    data = SensorData.objects.all().order_by("-timestamp")
    return render(request, "mqtt_app/sensor_data.html", {"data": data})
