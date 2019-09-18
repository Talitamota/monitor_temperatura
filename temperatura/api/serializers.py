from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError
from temperatura.models import City


class CidadeSerializer(ModelSerializer):

	def validate(self, data):
		if data['city']:
			cidade = City.objects.filter(city__iexact=data['city'])
		if cidade:
			raise ValidationError("cidade with this nome already exists.")
		return data

	class Meta:
		model = City
		fields = ['city', 'temperatures']
