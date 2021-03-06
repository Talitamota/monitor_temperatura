from monitor.celery import app
from django.apps import apps
from .servicos.get_temperatura import GetTemperature

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

@app.task
def delete_temperature():
	cities = City.objects.all()
	if cities:
		for city in cities:
			if city.temps.all().count() > 30:
				city.temps.first().delete()