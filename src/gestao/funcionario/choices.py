from django.utils.translation import gettext_lazy as _
from django.db import models


class Sexo(models.TextChoices):
    MASCULINO = 'Masulino', _('Masculino')
    FEMININO = 'Feminino', _('Feminino')
    OUTRO = 'Outro', _('Outro')
