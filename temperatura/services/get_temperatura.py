import datetime
import requests

from temperatura.models import City, Temperature

class GetTemperature:

	def get_woeid(self,cidade):
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

		woeid = response.json()['woeid']

		if woeid:

			return woeid

	def get_lista_cidades(self):
		lista = list(City.objects.all().values_list('city', flat=True))
		return lista

	def get_lista_woeids(self):
		lista_cidades = self.get_lista_cidades()
		lista_woeids = []
		if lista_cidades:
			lista_woeids = [self.get_woeid(cidade) for cidade in lista_cidades]
		return lista_woeids

	def get_temperatura(self, woeid):
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

	def get_temperature_list(self):
		lista_woeids = self.get_lista_woeids()
		lista_temperaturas = [self.get_temperatura(woeid) for woeid in lista_woeids]
		return lista_temperaturas