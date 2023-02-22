from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import  PessoaSexoSerializer
from apifile.models import Pessoa
from datetime import datetime
from tablib import Dataset
from django_filters.rest_framework import DjangoFilterBackend
from apifile.api.serializers import PessoaSerializer
from rest_framework import viewsets

class PessoaSexoViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all().order_by('-nascimento')
    serializer_class = PessoaSexoSerializer
    filter_backends = [DjangoFilterBackend]
    ordering = ['nome'] # ordenar por nome
    search_fields = ['sexo'] # pesquisa por sexo
    filterset_fields = ['sexo'] 

class PessoaViewSet(ModelViewSet):
    serializer_class = PessoaSerializer

    def create(self, request):
       # person_resource = PersonResource()
        dataset = Dataset()
        nova_perssoa = request.FILES.get('arquivo')
        import_dados = dataset.load(nova_perssoa.read(), format='xlsx')
        for dados in import_dados:
            valores = Pessoa(id_code=dados[1], 
                             nome=dados[2], 
                             sobrenome=dados[3], 
                             sexo=dados[4], 
                             altura=dados[5],
                             peso=dados[6], 
                             nascimento=datetime.utcfromtimestamp(dados[7]).strftime('%Y-%m-%d'),
                             bairro=dados[8], 
                             cidade=dados[9], 
                             estado=dados[10], 
                             numero=dados[11], )
            valores.save()
        response='Carregado com sucesso!'
        return Response(response)
    def get_queryset(self):
        return Pessoa.objects.all().filter(cidade='Meeren', sexo='F')

