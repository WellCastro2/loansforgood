from django.db import models

class Proposta(models.Model):

    PENDENTE = 1
    ANALISE = 2
    APROVADO = 3
    NEGADO = 4

    STATUS_CHOICES = (
        (PENDENTE, 'Pendente'),
        (ANALISE, 'Análise Manual'),
        (APROVADO, 'Aprovado'),
        (NEGADO, 'Negado'),
    )

    created_at = models.DateTimeField('Data de criação', auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField('Data atualização', auto_now=True, blank=False, null=False)
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDENTE)
    finalizada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class FormConfig(models.Model):

    TYPE_CHOICES = (
        ('text', 'text'),
        ('email', 'email'),
        ('number', 'number'),
    )

    campo = models.CharField("Nome do campo", max_length=100)
    label = models.CharField("Label para exibição do campo", max_length=100, default="label")
    tipo = models.CharField(choices=TYPE_CHOICES, max_length=10, default="text")
    exibir = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Formulário campos"
        verbose_name_plural = "Formulário campos"

    def __str__(self):
        return self.campo
