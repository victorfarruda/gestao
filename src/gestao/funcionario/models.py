from django.db import models

from gestao.departamento.models import Departamento
from gestao.funcionario.choices import Sexo


class Funcionario(models.Model):
    nome = models.CharField(max_length=120)
    cpf = models.CharField(max_length=30)
    rg = models.CharField(max_length=30)
    departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.SET_NULL)
    sexo = models.CharField(max_length=30, choices=Sexo.choices)
    data_nascimento = models.DateField()
    habilitacao = models.BooleanField()
    salario = models.FloatField()
    carga_horaria_semanal = models.IntegerField()

    class Meta:
       unique_together = (('nome', 'cpf', 'rg'),)
