from monitor.celery import app
import datetime
import requests

from temperatura.models import Cidade, Temperatura


def check_status_code(response):
	if response.status_code == 200:
		return response
	raise Exception(
		"StatusCode: {}\n{}".format(
			response.status_code,
			response.text
			)
	)


def get_woeid(cidade):
	request_inf = {
		'url': 'https://api.hgbrasil.com/stats/find_woeid?',
		'method': 'get',
		'data': {
			'key': '17284dd0',
			'format': 'json-cors',
			'sdk_version': 'console',
			'city_name': cidade
		},
	}

	response = requests.request(**request_inf)

	check_status_code(response)

	woeid = response.json()['woeid']

	if woeid:

		return woeid


def get_lista_cidades():
	lista = list(Cidade.objects.all().values_list('city', flat=True))
	return lista


def get_lista_woeids():
	lista_cidades = get_lista_cidades()
	lista_woeids = []
	if lista_cidades:
		lista_woeids = [get_woeid(cidade) for cidade in lista_cidades]
	return lista_woeids


def get_temperatura(woeid):
	request_inf = {
		'url': 'https://api.hgbrasil.com/weather?',
		'method': 'get',
		'data': {
			'woeid': woeid
		},
	}

	response = requests.request(**request_inf)

	temperatura = response.json()['results']

	return temperatura


def get_lista_temperaturas():
	lista_woeids = get_lista_woeids()
	lista_temperaturas = [get_temperatura(woeid) for woeid in lista_woeids]
	return lista_temperaturas	


@app.task
def testando_a_task():
	lista_temperaturas = get_lista_temperaturas()
	if lista_temperaturas:
		for temperatura in lista_temperaturas:
			cidade = Cidade.objects.filter(city__iexact=temperatura['city_name'])
			Temperatura.objects.create(
				valor=temperatura['temp'],
				data=temperatura['date'],
				hora=temperatura['time'],
				cidade=cidade[0]
			)
