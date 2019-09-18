from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError
from temperatura.models import Cidade


class CidadeSerializer(ModelSerializer):

	def validate(self, data):
		if data['city']:
			cidade = Cidade.objects.filter(city__iexact=data['city'])
		if cidade:
			raise ValidationError("cidade with this nome already exists.")
		return data

	class Meta:
		model = Cidade
		fields = ['city', 'temperatures']
