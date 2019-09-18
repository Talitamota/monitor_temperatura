from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError
from django.apps import apps

City = apps.get_model('temperatura.City')


class CitySerializer(ModelSerializer):

	def validate(self, data):
		if data['city']:
			city = City.objects.filter(city__iexact=data['city'])
		if city:
			raise ValidationError("cidade with this nome already exists.")
		return data

	class Meta:
		model = City
		fields = ['city', 'temperatures']
