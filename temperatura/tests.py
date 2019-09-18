from django.test import TestCase
from model_mommy import mommy

from temperatura.models import City, Temperature


class CityTestCase(TestCase):

	def setUp(self):
		self.city = mommy.make('City', city='São Paulo')

	def test_metodo_deve_retonar_lista_de_dicionarios_com_temperatura_e_com_data(self):
		city = self.city
		mommy.make('Temperature', temp='22', date='18/09/2019', time='17:55', city=self.city)
		mommy.make('Temperature', temp='23', date='18/09/2019', time='18:55', city=self.city)

		lista_de_dicionarios = [
			{
				'date': '18/09/2019 17:55',
				'temperature': '22',
			},
			{
				'date': '18/09/2019 18:55',
				'temperature': '23',
			}
		]
		self.assertEqual(city.temperatures(), lista_de_dicionarios )

	def test_metodo_save_deve_retornar_city_sem_acento_e_minuscula(self):
		self.assertEqual(self.city.city, 'sao paulo')

	def test_metodo_save_deve_retornar_custom_name_city_sem_espaco(self):
		self.assertEqual(self.city.custom_name_city, 'saopaulo')

