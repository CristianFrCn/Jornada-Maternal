from rest_framework import viewsets
from .serializers import GestanteSerializer
from .models import  import Gestante

class GestanteViewSet(viewsets.ModelViewSet):
    models = Gestante
    serializer_class = GestanteSerializer
    queryset = Gestante.objets.all()
    filter_fields = ('nome', 'cpf', 'idade','sus','endereco','genero','crianca')