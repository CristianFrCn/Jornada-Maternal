from .models import Gestante
from rest_framework import  serializers

class GestanteSerializers(serializers.modelsSerializers);
    class Meta:
        models = Gestante
        fields = ['nome', 'cpf', 'idade','sus','endereco','genero','crianca']