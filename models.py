# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alunos(models.Model):
    seq_geral = models.AutoField(primary_key=True)
    matricula = models.CharField(max_length=50, blank=True, null=True)
    nome = models.CharField(max_length=250, blank=True, null=True)
    nome_mae = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alunos'


class Amostranomes1(models.Model):
    tid = models.BigIntegerField(blank=True, null=True)
    nome = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amostranomes1'


class Amostranomes1Df(models.Model):
    token = models.IntegerField(primary_key=True)
    df = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amostranomes1_df'


class Amostranomes1Rawsetweight(models.Model):
    tid = models.IntegerField(primary_key=True)
    s1 = models.IntegerField(blank=True, null=True)
    s2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amostranomes1_rawsetweight'


class Amostranomes1Setweight(models.Model):
    tid = models.IntegerField(primary_key=True)
    sw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amostranomes1_setweight'


class Amostranomes1Size(models.Model):
    n = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amostranomes1_size'


class Amostranomes1Tokendf(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()
    df = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amostranomes1_tokendf'
        unique_together = (('tid', 'token'),)


class Amostranomes1Tokens(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'amostranomes1_tokens'
        unique_together = (('tid', 'token'),)


class Amostranomes1Weights(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()
    sw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amostranomes1_weights'
        unique_together = (('tid', 'token'),)


class Amostranomes2(models.Model):
    tid = models.BigIntegerField(blank=True, null=True)
    nome = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amostranomes2'


class Amostranomes2Df(models.Model):
    token = models.IntegerField(primary_key=True)
    df = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amostranomes2_df'


class Amostranomes2Rawsetweight(models.Model):
    tid = models.IntegerField(primary_key=True)
    s1 = models.IntegerField(blank=True, null=True)
    s2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amostranomes2_rawsetweight'


class Amostranomes2Setweight(models.Model):
    tid = models.IntegerField(primary_key=True)
    sw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amostranomes2_setweight'


class Amostranomes2Size(models.Model):
    n = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amostranomes2_size'


class Amostranomes2Tokendf(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()
    df = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amostranomes2_tokendf'
        unique_together = (('tid', 'token'),)


class Amostranomes2Tokens(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'amostranomes2_tokens'
        unique_together = (('tid', 'token'),)


class Amostranomes2Weights(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()
    sw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amostranomes2_weights'
        unique_together = (('tid', 'token'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cliente(models.Model):
    cpf = models.CharField(primary_key=True, max_length=15)
    nome = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    endereco = models.ForeignKey('Enderecos', models.DO_NOTHING, db_column='endereco')

    class Meta:
        managed = False
        db_table = 'clientes'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Enderecos(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=200, blank=True, null=True)
    bairro = models.CharField(max_length=200, blank=True, null=True)
    cidade = models.CharField(max_length=200, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enderecos'


class ItensVenda(models.Model):
    venda = models.ForeignKey('Vendas', models.DO_NOTHING, db_column='venda')
    cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='cliente')
    produto = models.ForeignKey('Produtos', models.DO_NOTHING, db_column='produto')

    class Meta:
        managed = False
        db_table = 'itens_venda'


class MyprojectPerson(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=30)
    age = models.IntegerField()
    active = models.BooleanField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'myproject_person'


class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produtos'


class SdmCatalog(models.Model):
    sourcetable = models.CharField(primary_key=True, max_length=128)
    keyattr = models.CharField(max_length=32, blank=True, null=True)
    targetattr = models.CharField(max_length=32, blank=True, null=True)
    q = models.IntegerField(blank=True, null=True)
    stage = models.IntegerField(blank=True, null=True)
    has_constraints = models.BooleanField(blank=True, null=True)
    updated = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sdm_catalog'


class SearchTokens(models.Model):
    tid = models.IntegerField(blank=True, null=True)
    token = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_tokens'


class Similares(models.Model):
    s1 = models.CharField(max_length=200, blank=True, null=True)
    sim = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    s2 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'similares'


class Socios(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)
    nomes = models.CharField(max_length=200, blank=True, null=True)
    tid = models.AutoField()

    class Meta:
        managed = False
        db_table = 'socios'


class Socios1(models.Model):
    nome = models.TextField(blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    tid = models.AutoField()

    class Meta:
        managed = False
        db_table = 'socios1'


class Socios1Df(models.Model):
    token = models.IntegerField(primary_key=True)
    df = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios1_df'


class Socios1Rawsetweight(models.Model):
    tid = models.IntegerField(primary_key=True)
    s1 = models.IntegerField(blank=True, null=True)
    s2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios1_rawsetweight'


class Socios1Setweight(models.Model):
    tid = models.IntegerField(primary_key=True)
    sw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios1_setweight'


class Socios1Size(models.Model):
    n = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios1_size'


class Socios1Tokendf(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()
    df = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios1_tokendf'
        unique_together = (('tid', 'token'),)


class Socios1Tokens(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'socios1_tokens'
        unique_together = (('tid', 'token'),)


class Socios1Weights(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()
    sw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios1_weights'
        unique_together = (('tid', 'token'),)


class Socios2(models.Model):
    nome = models.TextField(blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    tid = models.AutoField()

    class Meta:
        managed = False
        db_table = 'socios2'


class Socios2Df(models.Model):
    token = models.IntegerField(primary_key=True)
    df = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios2_df'


class Socios2Rawsetweight(models.Model):
    tid = models.IntegerField(primary_key=True)
    s1 = models.IntegerField(blank=True, null=True)
    s2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios2_rawsetweight'


class Socios2Setweight(models.Model):
    tid = models.IntegerField(primary_key=True)
    sw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios2_setweight'


class Socios2Size(models.Model):
    n = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios2_size'


class Socios2Tokendf(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()
    df = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios2_tokendf'
        unique_together = (('tid', 'token'),)


class Socios2Tokens(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'socios2_tokens'
        unique_together = (('tid', 'token'),)


class Socios2Weights(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()
    sw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios2_weights'
        unique_together = (('tid', 'token'),)


class SociosDf(models.Model):
    token = models.IntegerField(primary_key=True)
    df = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios_df'


class SociosRawsetweight(models.Model):
    tid = models.IntegerField(primary_key=True)
    s1 = models.IntegerField(blank=True, null=True)
    s2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios_rawsetweight'


class SociosSetweight(models.Model):
    tid = models.IntegerField(primary_key=True)
    sw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios_setweight'


class SociosSize(models.Model):
    n = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios_size'


class SociosTokendf(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()
    df = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios_tokendf'
        unique_together = (('tid', 'token'),)


class SociosTokens(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'socios_tokens'
        unique_together = (('tid', 'token'),)


class SociosWeights(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()
    sw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socios_weights'
        unique_together = (('tid', 'token'),)


class Trilhas(models.Model):
    nome = models.CharField(max_length=200, blank=True, null=True)
    cpf = models.CharField(max_length=200, blank=True, null=True)
    tid = models.AutoField()

    class Meta:
        managed = False
        db_table = 'trilhas'


class TrilhasDf(models.Model):
    token = models.IntegerField(primary_key=True)
    df = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trilhas_df'


class TrilhasRawsetweight(models.Model):
    tid = models.IntegerField(primary_key=True)
    s1 = models.IntegerField(blank=True, null=True)
    s2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trilhas_rawsetweight'


class TrilhasSetweight(models.Model):
    tid = models.IntegerField(primary_key=True)
    sw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trilhas_setweight'


class TrilhasSize(models.Model):
    n = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trilhas_size'


class TrilhasTokendf(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()
    df = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trilhas_tokendf'
        unique_together = (('tid', 'token'),)


class TrilhasTokens(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'trilhas_tokens'
        unique_together = (('tid', 'token'),)


class TrilhasWeights(models.Model):
    tid = models.IntegerField(primary_key=True)
    token = models.IntegerField()
    sw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trilhas_weights'
        unique_together = (('tid', 'token'),)


class Vendas(models.Model):
    id_venda = models.AutoField(primary_key=True)
    cliente = models.CharField(max_length=200, blank=True, null=True)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendas'
