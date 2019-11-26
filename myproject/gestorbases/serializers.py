from rest_framework import serializers
from myproject.gestorbases.models import Tabela
from myproject.gestorbases.models import Base

class TabelaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tabela
        fields = ['base', 'nome', 'descricao', 'esquema']


class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ['nome', 'descricao', 'atualizacao', 'host', 'owner']
