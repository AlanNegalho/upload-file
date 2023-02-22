from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apifile.models import Pessoa

class PessoaSerializer(ModelSerializer):
    data_nasc = serializers.DateTimeField(source="nascimento")
    class Meta:
        model = Pessoa
        fields = ['arquivo','id_code', 'nome', 'sobrenome',
                  'sexo', 'altura', 'peso','data_nasc', 
                  'bairro', 'cidade',
                  'estado', 'numero']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get('arquivo') is None:
            representation.pop('arquivo')
    
        return representation

class PessoaSexoSerializer(ModelSerializer):
    data_nasc = serializers.DateTimeField(source="nascimento")
    class Meta:
        model = Pessoa
        fields = ('id_code', 'nome', 'sobrenome',
                  'sexo', 'altura', 'peso',
                  'data_nasc', 'bairro', 'cidade',
                  'estado', 'numero',)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation.get('sobrenome') is None:
            representation.pop('sobrenome')
    
        return representation