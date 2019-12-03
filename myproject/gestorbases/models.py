from django.db import models
from django.utils.translation import ugettext_lazy as _

'''
    Classe que modela o objeto Base é convertida em uma tabela do banco de dados
'''
class Base(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.TextField(null=True, blank=False)
    atualizacao = models.DateField('Data de atualizacao', null=True, blank=True)
    host = models.CharField(max_length=255, null=True, blank=False)
    owner = models.CharField(max_length=255, null=True, blank=True)
    objetos = models.Manager()

    def __str__(self):
        return self.nome


'''
    Classe que modela o objeto Tabela é convertida em uma tabela do banco de dados
'''
class Tabela(models.Model):
    base = models.ForeignKey(Base, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, null=True, blank=False, unique=True)
    descricao = models.TextField(max_length=255, null=True, blank=True)
    esquema = models.CharField(max_length=255, null=True, blank=True)
    objetos = models.Manager()

    def __str__(self):
        return self.nome
     

'''
    Classe que modela uma atualização é convertida em uma tabela do banco de dados
'''
class Atualizacao(models.Model):
    tabela = models.ForeignKey(Tabela, on_delete=models.CASCADE)
    data_atualizacao = models.DateField('Data da atualizacao', auto_now_add=True)
    responsavel = models.CharField(max_length=255, null=False, blank=False)
    observacoes = models.TextField(null=True, blank=True)
    mes_ref = models.IntegerField(null=True, blank=True)
    ano_ref = models.IntegerField(null=True, blank=True)
    reg_alt = models.IntegerField(null=True, blank=True)
    origem_dados = models.CharField(max_length=255, null=True, blank=False)
    objetos = models.Manager()

    def __str__(self):
        return self.tabela.nome



from django.db import models
from django.contrib.auth.signals import user_logged_in, user_logged_out  

class LoggedUser(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    objetos = models.Manager()


    def __unicode__(self):
        return self.username

    
    def inserteLoggedUser(self, request):
        usuario = request.POST.get('usuario')
        user = LoggedUser(username=usuario)
        user.save()
        

    def __str__(self):
        return self.username

      
