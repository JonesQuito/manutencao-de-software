from django.contrib import admin
from django.urls import path
from myproject.gestorbases import views

app_name='gestorbases'

urlpatterns = [
	#path('', views.home, name='home'),
	path('', views.dashboard, name='dashboard'),


	path('bases/nova', views.BaseCreateView.as_view(), name='nova_base'),
	#path('bases/lista', views.BaseListView.as_view(), name='lista_bases'),
	path('bases/lista', views.listingBases, name='lista_bases'),
	path('bases/atualiza/<pk>', views.BaseUpdateView.as_view(), name='atualiza_base'),
	path('bases/exclui/<pk>', views.BaseDeleteView.as_view(), name='exclui_base'),


	path('tabelas/nova', views.TabelaCreateView.as_view(), name='nova_tabela'),
	#path('tabelas/lista', views.TabelaListView.as_view(), name='lista_tabelas'),
	path('tabelas/lista', views.listingTables, name='lista_tabelas'),
	path('tabelas/atualiza/<pk>', views.TabelaUpdateView.as_view(), name='atualiza_tabela'),
	path('tabelas/exclui/<pk>', views.TabelaDeleteView.as_view(), name='exclui_tabela'),


	#path('atualizacoes/nova', views.AtualizacaoCreateView.as_view(), name='nova_atualizacao'),
	path('atualizacoes/nova2/<pk>,<tab_nome>', views.novaAtualizazao, name='nova_atualizacao2'),
	path('atualizacoes/nova/<pk>', views.AtualizacaoCreateView2.as_view(), name='nova_atualizacao3'),

	#path('atualizacoes/lista', views.AtualizacaoListView.as_view(), name='lista_atualizacoes'),
	path('atualizacoes/lista', views.listingAtualizacoes, name='lista_atualizacoes'),
	path('atualizacoes/detalhes/<pk>', views.AtualizacaoDetalhesView.as_view(), name='detalhes_atualizacao'),
	path('atualizacoes/atualiza/<pk>', views.AtualizacaoUpdateView.as_view(), name='atualiza_atualizacao'),
	path('atualizacoes/exclui/<pk>', views.AtualizacaoDeleteView.as_view(), name='exclui_atualizacao'),

	path('atualizacoes/chart', views.getAtualizacoes, name='atualizacoes_chart'),

	path('login/', views.login, name='login'),
	path('sair/', views.sair, name='sair'),

    path('admin/', admin.site.urls),
]