from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Person(models.Model):
    name = models.CharField(_('Nome'), max_length=50)
    email = models.EmailField(_('e-mail'), max_length=30, unique=True)
    age = models.IntegerField(_('Idade'))
    active = models.BooleanField(_('Ativo'), default=True)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True, auto_now=False)

    persons = models.Manager()

    class Meta:
        ordering = ['name']
        verbose_name = "pessoa"
        verbose_name_plural = "pessoas"



class Funcionario(models.Model):

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    tempo_de_servico = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    remuneracao = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )

    objetos = models.Manager()

