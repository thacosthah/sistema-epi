from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Colaborador, Equipamento, EmprestimoEPI

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'cargo')
    search_fields = ('nome', 'cpf')

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade_estoque')
    search_fields = ('nome',)

@admin.register(EmprestimoEPI)
class EmprestimoEPIAdmin(admin.ModelAdmin):
    list_display = ('colaborador', 'equipamento', 'quantidade', 'data_emprestimo', 'status')
    list_filter = ('status', 'data_emprestimo')
    search_fields = ('colaborador__nome', 'equipamento__nome')

# Regista o User com o UserAdmin padrão do Django para corrigir a gestão de permissões
admin.site.unregister(User)
admin.site.register(User, UserAdmin)