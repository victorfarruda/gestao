from django.db import models

from gestao.departamento.models import Departamento
from gestao.funcionario.models import Funcionario


class Projeto(models.Model):
    nome = models.CharField(max_length=120)
    departamento = models.ForeignKey(Departamento, null=True, blank=True, on_delete=models.SET_NULL)
    horas_para_concluir_projeto = models.IntegerField()
    data_prazo_estimado = models.DateField()
    horas_realizadas = models.IntegerField()
    data_ultimo_calculo_horas = models.DateField()
    supervisor = models.ForeignKey(Funcionario, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
       unique_together = (('nome', 'departamento'),)
