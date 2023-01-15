from django.db import models

# Create your models here.

SEXO_CHOICES = (
    ('M','masculino'),
    ('F','feminino'),
)

class Pessoa(models.Model):
    id_code = models.CharField(max_length=30,null=True)
    nome = models.CharField(max_length=45,null=True)
    sobrenome = models.CharField(max_length=45, null=True, blank=True)
    sexo = models.CharField(max_length=2, choices=SEXO_CHOICES,null=True)
    altura = models.FloatField(null=True, blank=True, default=None)
    peso = models.FloatField(null=True, blank=True, default=None)
    nascimento = models.DateTimeField(verbose_name="Data", null=True)
    bairro = models.CharField(max_length=35,null=True)
    cidade = models.CharField(max_length=25,null=True)
    estado = models.CharField(max_length=25,null=True)
    numero = models.DecimalField(max_digits=8, decimal_places=0,null=True)
    arquivo= models.FileField(null=True)
    
    def __str__(self):
        return self.nome

    def get_nascimento(self):
        return self.nascimento.strftime('%d/%m/%Y')
