from monitor.celery import app
from django.apps import apps
from .services.get_temperatura import GetTemperature

City = apps.get_model('temperatura.City')
Temperature = apps.get_model('temperatura.Temperature')

@app.task
def get_temperature():
	temperature = GetTemperature()
	temperature_list = temperature.get_temperature_list()

	if temperature_list:
		for temperature in temperature_list:
			city = City.objects.filter(city__iexact=temperature['city_name'])
			Temperature.objects.create(
				temp=temperature['temp'],
				date=temperature['date'],
				time=temperature['time'],
				city=city[0]
			)
