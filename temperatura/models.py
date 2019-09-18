from unidecode import unidecode
from django.db import models



class Cidade(models.Model):
	city = models.CharField(max_length=100, unique=True)
	custom_city = models.CharField(max_length=100, unique=True)
	woeid = models.CharField(max_length=100, blank=True)

	def temperatures(self):
		temperaturas = self.temperaturas.all()
		dicionario = {}
		lista_dicionarios = []
		if temperaturas:
			for temperatura in temperaturas:
				dicionario = {
					'date': temperatura.data +' '+ temperatura.hora,
					'temperature': temperatura.valor
				}
				lista_dicionarios.append(dicionario)
		return lista_dicionarios

	def __str__(self):
		return self.city

	def save(self, *args, **kwargs):
		self.custom_city = self.city.lower().replace(' ','')
		self.city = self.city.lower().title()
		super(Cidade, self).save(*args, **kwargs)


class Temperatura(models.Model):
	valor = models.CharField(max_length=2)
	data = models.CharField(max_length=10)
	hora = models.CharField(max_length=5)
	cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, related_name='temperaturas')

	def __str__(self):
		return str(self.valor)

