from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=120, unique=True)
    data_nascimento = models.DateField()
    habilitacao = models.BooleanField()
    salario = models.FloatField()
    carga_horaria_semanal = models.IntegerField()
