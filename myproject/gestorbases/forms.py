from django import forms
from myproject.gestorbases.models import Base, Tabela , Atualizacao


# FORMULÁRIO DE INCLUSÃO DE BASES
# -------------------------------------------
class InsereBaseForm(forms.ModelForm):
	
	class Meta:
		# Modelo 
		model = Base
		# Campos que estarão no form
		fields = ['nome', 'descricao', 'atualizacao', 'host', 'owner']


# FORMULÁRIO DE INCLUSÃO DE TABELAS
# -------------------------------------------
class InsereTabelaForm(forms.ModelForm):
    class Meta:
        # Modelo
        model = Tabela
        # Campos que estarão no form
        fields = ['base', 'nome', 'descricao', 'esquema']


# FORMULÁRIO DE INCLUSÃO DE NOVA ATUALIZAÇÃO
# -------------------------------------------
class InsereAtualizacaoForm(forms.ModelForm):
    class Meta:
        # Modelo
        model = Atualizacao
        # Campos que estarão no fomr
        fields = ['tabela', 'responsavel', 'observacoes', 'mes_ref', 'ano_ref', 'origem_dados']


    def filteringTables(self, request):
        tabela = request.GET.get('tabela')
        tabelas = Tabela.objetos.filter(nome__icontains=tabela)
        return tabelas

        
