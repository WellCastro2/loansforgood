from rest_framework import serializers
from django.core.exceptions import ValidationError

from core.models import Proposta, FormConfig


class PropostaSerializer(serializers.ModelSerializer):

    def validate_cpf(self, value):
        cpf = str(value)

        if len(cpf) != 11 or not cpf.isdigit():
            raise ValidationError('CPF inválido.')
    
        return value


    class Meta:
        model = Proposta
        fields = ['cpf', 'nome', 'status',]


class FormSerializer(serializers.ModelSerializer):

    class Meta:
        model = FormConfig
        fields = ['campo', 'tipo', 'label']
