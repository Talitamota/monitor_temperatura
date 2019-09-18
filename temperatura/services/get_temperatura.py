import datetime
import requests
from django.apps import apps

City = apps.get_model('temperatura.City')
Temperature = apps.get_model('temperatura.Temperature')


class GetTemperature:

	def get_woeid(self,city):
		request_inf = {
			'url': 'https://api.hgbrasil.com/stats/find_woeid?',
			'method': 'get',
			'data': {
				'key': '17284dd0',
				'format': 'json-cors',
				'sdk_version': 'console',
				'city_name': city
			},
		}

		response = requests.request(**request_inf)

		woeid = response.json()['woeid']

		if woeid:

			return woeid

	def get_cities_list(self):
		return list(City.objects.all().values_list('city', flat=True))

	def get_woeids_list(self):
		cities_list = self.get_cities_list()
		woeids_list = []
		if cities_list:
			woeids_list = [self.get_woeid(city) for city in cities_list]
		return woeids_list

	def get_temperature(self, woeid):
		request_inf = {
			'url': 'https://api.hgbrasil.com/weather?',
			'method': 'get',
			'data': {
				'woeid': woeid
			},
		}

		response = requests.request(**request_inf)

		temperature = response.json()['results']

		return temperature

	def get_temperature_list(self):
		woeids_list = self.get_woeids_list()
		temperature_list = [self.get_temperature_list(woeid) for woeid in woeids_list]
		return temperature_list