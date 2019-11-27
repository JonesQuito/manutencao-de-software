# DEPENDÊNCIAS NECESSÁRIAS PARA REDIRECIONAR E RENDERIZAR TEMPLATES
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse


# DEPENDÊNCIAS NECESSÁRIAS PARA TEMPLATES
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import View

# IMPORTANDO OS FORMS DA APLICAÇÃO
from myproject.gestorbases.forms import InsereBaseForm
from myproject.gestorbases.forms import InsereTabelaForm
from myproject.gestorbases.forms import InsereAtualizacaoForm

# IMPORTANDO OS MODELS DA APLICAÇÃO
from myproject.gestorbases.models import Base
from myproject.gestorbases.models import Tabela
from myproject.gestorbases.models import Atualizacao
from myproject.gestorbases.models import LoggedUser

# DEPENDÊNCIAS NECESSÁRIAS PARA IMPLEMENTAR A PAGINAÇÃO
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator

# DEPENDÊNCIAS NECESSÁRIAS PARA IMPLEMENTAR A LOGIN
from django.contrib.auth import authenticate, logout, login as authlogin
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required, permission_required


from django.contrib import messages

from django.db import connection

# DEPENDÊNCIAS NECESSÁRIAS PARA SERIALIZAR DADOS EM JSON
import json



# ########################### VIEWS DE LOGIN ##########################
"""
	Responsável por direcionar o usuário para a view de login caso tente acessar qualquer página
	da aplicação sem está devidamente autenticado
"""

def inserteLoggedUser(request):
    usuario = request.POST.get('usuario')
    user = LoggedUser(username=usuario)
    user.save()

def deleteLoggedUser(request, pk):
	try:
		username = request.POST.get('pk')
		u = LoggedUser.objetos.filter(username=pk).first()
		print(u)
		u.delete()

	except LoggedUser.DoesNotExist:
		pass



def login(request):
	if request.user.id:
		return render(request, 'gestorbases/logado.html',{})
	if request.POST:
		usuario = request.POST.get('usuario')
		senha = request.POST.get('senha')
		u = authenticate(request, username=usuario, password=senha)

		if(u is not None):
			if(u.is_active):
				authlogin(request, u)
				inserteLoggedUser(request)
				return redirect('gestorbases:dashboard')
				#return render(request, 'gestorbases/dashboard.html',{'user': u})
	return render(request, 'gestorbases/login.html', {})

def sair(request, pk):
	logout(request)
	deleteLoggedUser(request, pk)
	return render(request, 'gestorbases/login.html', {})
# ########################### SISTEMA DE LOGIN ##########################


# RENDERIZAR O DASHBOARD
@login_required
def dashboard(request):
	if request.user.is_authenticated:
		cursor = connection.cursor()
		cursor.execute("select * from count_users")
		bases = Base.objetos.all()
		tabelas = Tabela.objetos.all()
		atualizacoes = Atualizacao.objetos.all()
		
		request.session['count_user'] = LoggedUser.objetos.count()
		count_user = request.session.get('count_user')

		contexto = {'tabelas': tabelas, 'bases': bases, 'atualizacoes': atualizacoes, 'count_user':count_user}
		return render(request, 'gestorbases/dashboard.html', contexto)


# CADASTRAMENTO DE BASE
# ----------------------------------------------
class BaseCreateView(LoginRequiredMixin, CreateView):
    template_name = 'gestorbases/base/cadastroBase.html'
    model = Base
    form_class = InsereBaseForm
    success_url = reverse_lazy("gestorbases:lista_bases")

def cadastroBase(request):
	if request.POST:
		nome = request.POST.get('nome')
		descricao = request.POST.get('descricao')
		host = request.POST.get('host')
		owner = request.POST.get('owner')
		# verifica se já há uma base com o nome informado
		bases = Base.objetos.filter(nome=nome)
		if len(bases) > 0:
			messages.add_message(request, messages.INFO, 'Já existe uma base com o nome '+ nome+ '!')
			contexto = {'nome': nome, 'descricao': descricao, 'host': host, 'owner':owner}
			return render(request, 'gestorbases/base/novaBase.html', contexto)

		base = Base(nome=nome,descricao=descricao, host=host, owner=owner)
		baseName = Base.objetos.filter(nome__icontains=base)
		base.save()
		return redirect('gestorbases:lista_bases')
	else:
		return render(request, 'gestorbases/base/novaBase.html', {})
    

	
# LISTAGEM DE BASES COM PAGINAÇÃO
# ----------------------------------------------
@login_required
def listingBases(request):
	bases_lista = Base.objetos.all().order_by('id')
	paginator = Paginator(bases_lista, 7)
	page = request.GET.get('page')
	bases = paginator.get_page(page)
	return render(request, 'gestorbases/base/listaBases.html', {'bases':bases})

# ATUALIZAÇÃO DE BASE
# ----------------------------------------------
class BaseUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'gestorbases/base/editaBase.html'
	model = Base
	fields = '__all__'
	context_object_name = 'base'
	success_url = reverse_lazy("gestorbases:lista_bases")


# EXCLUSÃO DE BASE
# ----------------------------------------------
class BaseDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'gestorbases/base/excluiBase.html'
	model = Base
	fields = '__all__'
	context_object_name = 'base'
	success_url = reverse_lazy('gestorbases:lista_bases')



# CADASTRO DE TABELA
# ----------------------------------------------
from django.http import HttpResponse
class TabelaCreateView(LoginRequiredMixin, CreateView):
	template_name = 'gestorbases/tabela/cadastroTabela.html'
	model = Tabela
	form_class = InsereTabelaForm
	success_url = reverse_lazy('gestorbases:lista_tabelas')

	def form_invalid(self, form):
		messages.add_message(self.request, messages.INFO, 'Já existe uma tabela com o nome informado!')
		return redirect('gestorbases:nova_tabela')

	def form_valid(self, form):
		return super(TabelaCreateView, self).form_valid(form)
		

# LISTAGEM DE TABELAS COM PAGINAÇÃO
# ----------------------------------------------
@login_required
def listingTables(request):
	if request.GET.get('tabela') == None:
		tabelas_lista = Tabela.objetos.all()[:100]
		paginator = Paginator(tabelas_lista, 7)
		page = request.GET.get('page')
		tabelas = paginator.get_page(page)
		return render(request, 'gestorbases/tabela/listaTabelas.html', {'tabelas': tabelas})
	else:
		tab = request.GET.get('tabela')
		tabelas_lista = Tabela.objetos.filter(nome__icontains=tab)[:100]
		paginator = Paginator(tabelas_lista, 7)
		page = request.GET.get('page')
		tabelas = paginator.get_page(page)
		return render(request, 'gestorbases/tabela/listaTabelas.html', {'tabelas': tabelas})


@login_required
def listingUsuarios(request):
	usuarios_lista = LoggedUser.objetos.all()
	print(usuarios_lista)
	paginator = Paginator(usuarios_lista, 7)
	page = request.GET.get('page')
	usuarios = paginator.get_page(page)
	print(usuarios)
	return render(request, 'gestorbases/usuario/listausuariosLogados.html', {'usuarios': usuarios})




# EDIÇÃO DE TABELAS
# ----------------------------------------------
class TabelaUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'gestorbases/tabela/editaTabela.html'
	models = Tabela
	fields = '__all__'
	context_object_name = 'tabela'
	success_url = reverse_lazy('gestorbases:lista_tabelas')


	def get_object(self, queryset=None):
		tabela = None
		id = self.kwargs.get(self.pk_url_kwarg)
		if id is not None:
			# Busca o tabela apartir do id
			tabela = Tabela.objetos.filter(id=id).first()

		# Retorna o objeto encontrado
		return tabela
		

# EXCLUSÃO DE TABELA
# ----------------------------------------------
class TabelaDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'gestorbases/tabela/excluiTabela.html'
	model = Tabela
	fields = '__all__'
	context_object_name = 'tabela'
	success_url = reverse_lazy('gestorbases:lista_tabelas')



# REGISTRO DE NOVA ATUALIZAÇÃO
# ----------------------------------------------

class AtualizacaoCreateView(LoginRequiredMixin, CreateView):
	template_name = 'gestorbases/atualizacao/cadastroAtualizacao.html'
	model = Atualizacao
	InsereAtualizacaoForm.tabela = Tabela.objetos.all()[:5]
	form_class = InsereAtualizacaoForm
	success_url = reverse_lazy('gestorbases:nova_atualizacao')


def novaAtualizazao(request, pk, tab_nome):
	if request.POST:
		tabela_id = request.POST.get('tabela')
		tabela = Tabela.objetos.filter(id=tabela_id).first()
		responsavel = request.POST.get('responsavel')
		origem_dados = request.POST.get('origem_dados')
		mes_ref = request.POST.get('mes_ref')
		ano_ref = request.POST.get('ano_ref')
		observacao = request.POST.get('observacao')
		atualizacao = Atualizacao(tabela=tabela, responsavel=responsavel, observacoes=observacao, mes_ref=mes_ref, ano_ref=ano_ref, origem_dados=origem_dados)
		atualizacao.save()
		print('ssssss')
		return redirect('gestorbases:lista_atualizacoes')
	else:
		context = {
			'tabela': tab_nome, 'pk':pk
		}
		return render(request, 'gestorbases/atualizacao/novaAtualizacao.html', context)

class AtualizacaoCreateView2(LoginRequiredMixin, CreateView):
	template_name = 'gestorbases/atualizacao/novaAtualizacao.html'
	model = Atualizacao
	InsereAtualizacaoForm.tabela = Tabela.objetos.all()[:5]
	form_class = InsereAtualizacaoForm
	success_url = reverse_lazy('gestorbases:nova_atualizacao')

	def get_object(self, queryset=None):
		tabela = None
		id = self.kwargs.get(self.pk_url_kwarg)
		if id is not None:
			tabela = Tabela.objetos.filter(id=id).first()
		return tabela


# FAZ PAGINAÇÃO DE ATUALIZAÇÃO
# ----------------------------------------------
@login_required
def listingAtualizacoes(request):
	if request.GET.get('tabela') != None and request.GET.get('data') != None:
		tab = request.GET.get('tabela')
		date = request.GET.get('data')
		atualizacoes = getUpdateByTableAndDate(request, tab, date)
		contexto = {'atualizacoes': atualizacoes, 'nomeTabela':tab, 'data':date}
		return render(request, 'gestorbases/atualizacao/listaAtualizacoes.html', contexto)
	elif request.GET.get('tabela') != None:
		tab = request.GET.get('tabela')
		atualizacoes = getUpdateByTables(request, tab)
		contexto = {'atualizacoes': atualizacoes, 'nomeTabela':tab}
		return render(request, 'gestorbases/atualizacao/listaAtualizacoes.html', contexto)
	elif request.GET.get('tabela') == None:		
		atualizacoes = getAllUpdates(request)
		messages.add_message(request, messages.INFO, 'Hello world.')
		#messages = ['Atualização registrada!!']
		contexto = {'atualizacoes': atualizacoes}
		return render(request, 'gestorbases/atualizacao/listaAtualizacoes.html', contexto)
	else:
		tab = request.GET.get('tabela')
		date = request.GET.get('data')
		atualizacoes = getUpdateByTableAndDate(request, tab, date)
		#atualizacoes = getUpdateByTables(request, tab)
		contexto = {'atualizacoes': atualizacoes, 'nomeTabela':tab, 'data':date}
		return render(request, 'gestorbases/atualizacao/listaAtualizacoes.html', contexto)
	

def getAllUpdates(request):
	atualizacoes_lista = Atualizacao.objetos.all().order_by('pk')
	paginator = Paginator(atualizacoes_lista, 5)
	page = request.GET.get('page')
	return paginator.get_page(page)

def getUpdateByTables(request, tab):
	tabelas = Tabela.objetos.filter(nome__icontains=tab)
	condicao = ''
	for tabela in tabelas:
		if condicao != '':
			condicao = condicao + ', ' + str(tabela.id)
		else:
			condicao = condicao + str(tabela.id)
	condicao = "(" + condicao + ")"
	if condicao == '()':
		condicao = '(-1)'
	atualizacoes_lista = Atualizacao.objetos.raw("select * from gestorbases_atualizacao where tabela_id in " + condicao)
	paginator = Paginator(atualizacoes_lista, 5)
	page = request.GET.get('page')
	return paginator.get_page(page)


## Disponibiliza o serviço de listagem de atualizações para ser consumido via ajax
def getAtualizacoes(request):
	from django.db import connection
	atualizacoes = []
	cursor = connection.cursor()
	cursor.execute("select to_char(data_atualizacao, 'DD/MM/yyyy'), count(*) from gestorbases_atualizacao where data_atualizacao > current_date - INTERVAL '365 DAYS' group by data_atualizacao order by data_atualizacao")
	for atualizacao in cursor:
		atualizacoes.append(atualizacao)


	if request.is_ajax():
		contexto = {'atualizacoes':atualizacoes}
		return HttpResponse(json.dumps(contexto), content_type='application/json')
	else:
		for atualizacao in atualizacoes:
			print(atualizacao)
		contexto = {'atualizacoes': atualizacoes}
		return HttpResponse(json.dumps(contexto), content_type='application/json')

	
'''
def getUpdateByDate(request, date):
	date = "'" + date + "'"
	atualizacoes_lista = Atualizacao.objetos.raw("select * from gestorbases_atualizacao where data_atualizacao >= " + date)
'''
def getUpdateByTableAndDate(request, tab, date):
	tabelas = Tabela.objetos.filter(nome__icontains=tab)
	condicao = ''
	for tabela in tabelas:
		if condicao != '':
			condicao = condicao + ', ' + str(tabela.id)
		else:
			condicao = condicao + str(tabela.id)
	condicao = "(" + condicao + ")"
	if condicao == '()':
		condicao = '(-1)'
	if date == '':
		date = '01/01/1970'

	sql = "select * from gestorbases_atualizacao where tabela_id in " + condicao + " and data_atualizacao >= '" + date + "'"
	print(sql)
	atualizacoes_lista = Atualizacao.objetos.raw(sql)
	paginator = Paginator(atualizacoes_lista, 5)
	page = request.GET.get('page')
	return paginator.get_page(page)


# DETALHAMENTO DE ATUALIZAÇÃO
# ----------------------------------------------
class AtualizacaoDetalhesView(LoginRequiredMixin, UpdateView):
	template_name = 'gestorbases/atualizacao/detalhesAtualizacao.html'
	model = Atualizacao
	fields = '__all__'
	context_object_name = 'atualizacao'

	def get_object(self, queryset=None):
		atualizacao = None
		id = self.kwargs.get(self.pk_url_kwarg)
		if id is not None:
			atualizacao = Atualizacao.objetos.filter(id=id).first()
		return atualizacao


# ATUALIZA DE REGISTRO DE ATUALIZAÇÃO
# ----------------------------------------------
class AtualizacaoUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'gestorbases/atualizacao/editaAtualizacao.html'
	model = Atualizacao
	fields = '__all__'
	context_object_name = 'atualizacao'
	success_url = reverse_lazy('gestorbases:lista_atualizacoes')

	def get_object(self, queryset=None):
		atualizacao = None
		id = self.kwargs.get(self.pk_url_kwarg)
		if id is not None:
			atualizacao = Atualizacao.objetos.filter(id=id).first()
		return atualizacao


# EXCLUSÃO DE REGISTRO DE ATUALIZAÇÃO
# ----------------------------------------------
class AtualizacaoDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'gestorbases/atualizacao/excluiAtualizacao.html'
	model = Atualizacao
	fields = '__all__'
	context_object_name = 'atualizacao'
	success_url = reverse_lazy('gestorbases:lista_atualizacoes')



# ##############  VIEWS DE TESTE ####################
'''
	As views abaixo foram implementadas para fins de teste durante o desenvolvimento da aplicação.
	Não interferem no funcionamento da mesma em produção
'''
from django.http import HttpResponse
from django.core import serializers
import json
from django.http import Http404
from rest_framework import serializers



def teste(request):
	tabelas = Tabela.objetos.all()
	if request.POST:
		tabela = request.POST.get('tabela')
		tabelas = Tabela.objetos.filter(nome__icontains=tabela)
		return render(request,'gestorbases/teste.html', {'tabelas':tabelas})
	return render(request,'gestorbases/teste.html', {'tabelas':tabelas})



def teste2(request, tablename):
	tabelas = Tabela.objetos.filter(nome__icontains=tablename)
	return JsonResponse(serializer.data, safe=False)
	
	#tabelas = [ tabela_serializer(tabela) for tabela in tabelas]
	#return HttpResponse(tabelas, content_type='application/json')
	#return render(request, 'gestorbases/teste.html', {'tabelas':tabelas})

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myproject.gestorbases.serializers import TabelaSerializer
from myproject.gestorbases.serializers import BaseSerializer

@csrf_exempt
def tabela_serializer(request, tablename):
	if request.method == 'GET':
		tabelas = Tabela.objetos.filter(nome=tablename)
		serializer = TabelaSerializer(tabelas, many=True)
		return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def base_serializer(request, basename):
	if request.method == 'GET':
		bases = Base.objetos.filter(nome=basename)
		serializer = BaseSerializer(bases, many=True)
		return JsonResponse(serializer.data, safe=False)




















