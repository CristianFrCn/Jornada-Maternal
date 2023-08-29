from rest_framework import viewsets
from .serializers import ClienteSerializer
from .models import Cliente

class ClienteViewSet(viewsets.ModelViewSet):
    model = Cliente
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    filter_fields = ('nome', 'cpf', 'idade','sus','endereco','genero','crianca')