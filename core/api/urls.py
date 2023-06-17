from django.urls import path
from core.api import views

urlpatterns = [
    path('formulario/', views.FormView.as_view(), name='formulario-list'),
    path('pedido/', views.PropostaView.as_view(), name='proposta'),
    path('pedidos/<str:cpf>', views.PedidosView.as_view(), name='proposta-list'),
]
