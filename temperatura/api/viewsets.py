from rest_framework.viewsets import ModelViewSet
from temperatura.models import Cidade
from .serializers import CidadeSerializer


class CidadeViewSet(ModelViewSet):

	queryset = Cidade.objects.all()
	serializer_class = CidadeSerializer
	lookup_field = 'custom_city'
