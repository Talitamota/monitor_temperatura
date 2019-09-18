from monitor.celery import app

from temperatura.models import City, Temperature

from .services.get_temperatura import GetTemperatura


@app.task
def atualiza_temperatura():
	get_temperatura = GetTemperatura()
	lista_temperaturas = get_temperatura.get_lista_temperaturas()
	if lista_temperaturas:
		for temperatura in lista_temperaturas:
			cidade = City.objects.filter(city__iexact=temperatura['city_name'])
			Temperature.objects.create(
				temp=temperatura['temp'],
				date=temperatura['date'],
				time=temperatura['time'],
				city=cidade[0]
			)
