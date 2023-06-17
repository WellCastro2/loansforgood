from django.contrib import admin
from .models import Proposta, FormConfig

@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome', 'status', 'finalizada')
    list_filter = ('status', 'finalizada')
    search_fields = ('cpf', 'nome')

@admin.register(FormConfig)
class FormConfigAdmin(admin.ModelAdmin):
    list_display = ('campo', 'exibir')
    list_filter = ('exibir',)
    list_editable = ('exibir',)
    search_fields = ('campo',)

admin.site.site_header = "Loans for good admin"
