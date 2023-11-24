from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf', 'email')
    search_fields = ('nome', 'sobrenome', 'cpf', 'email')
