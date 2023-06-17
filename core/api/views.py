from rest_framework import generics
from core.models import Proposta, FormConfig
from core.api.serializers import PropostaSerializer, FormSerializer


class FormView(generics.ListAPIView):
    queryset = FormConfig.objects.filter(exibir=True)
    serializer_class = FormSerializer


class PropostaView(generics.CreateAPIView):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer


class PedidosView(generics.RetrieveAPIView):
    queryset = Proposta.objects.all()
    serializer_class = PropostaSerializer
    lookup_field = 'cpf'
