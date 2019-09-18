from unidecode import unidecode
from django.db import models


class City(models.Model):
	city = models.CharField(max_length=100, unique=True)
	custom_name_city = models.CharField(max_length=100, unique=True)
	woeid = models.CharField(max_length=100, blank=True)

	def temperatures(self):
		temperatures = self.temps.all()
		dictionary = {}
		list_dictionaries = []
		if temperatures:
			for temperature in temperatures:
				dictionary = {
					'date': temperature.date +' '+ temperature.time,
					'temperature': temperature.temp
				}
				list_dictionaries.append(dictionary)
		return list_dictionaries

	def save(self, *args, **kwargs):
		self.city = unidecode(self.city).lower()
		self.custom_name_city = self.city.replace(' ','')
		super(City, self).save(*args, **kwargs)

	def __str__(self):
		return self.city


class Temperature(models.Model):
	temp = models.CharField(max_length=2)
	date = models.CharField(max_length=10)
	time = models.CharField(max_length=5)
	city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='temps')

	def __str__(self):
		return str(self.temp)

