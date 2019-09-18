from rest_framework.viewsets import ModelViewSet
from temperatura.models import City
from .serializers import CitySerializer


class CidadeViewSet(ModelViewSet):

	queryset = City.objects.all()
	serializer_class = CitySerializer
	lookup_field = 'custom_name_city'
