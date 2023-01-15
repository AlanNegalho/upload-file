from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from apifile.models import Pessoa


# Register your models here.

@admin.register(Pessoa)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('nome', 'sobrenome', 'sexo',
                    'altura', 'peso', 'nascimento',
                    'bairro', 'cidade', 'estado', 'numero')
    list_filter = ( 'nome', )

