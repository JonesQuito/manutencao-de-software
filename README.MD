## PROCEDIMENTOS PARA INSTALAÇÃO DO PROJETO

### INSTALAR O PYTHON 3.7 E CONFIGURAR A VARIÁVEL DE AMBINETE


### INSTALAR O VIRTUALENV VIA PIP
`pip install virtualenv` 

### CRIAR UM AMBINETE VIRTUAL
`virtualenv nome_do_ambiente`

### CLONAR O PROJETO DENTRO DO AMBINETE VIRTUAL CRIADO (USAR O GIT BASH)
`git clone https://github.com/JonesQuito/manutencao-de-software.git`

### ATIVANDO O AMBIENTE VIRTUAL
é necessário estar na raiz do ambiente virtual e executar o seguinte comando `Script\activate` (no Windows).

### INSTALAR AS BIBLIOTECAS REQUERIDAS PARA O PROJETO (o ambiente virtual deve está ativado)
(de dentro da pasta clonada executar) `pip install -r requirements.txt`

### EXECUTAR OS COMANDOS ABAIXO, CASO O COMANDO ANTERIOR FALHE
 - pip install Django
 - pip install psycopg2
 - pip install djangorestframework
 - pip install django-widget-tweaks
 - pip install django-global-permissions


O sistema faz acesso a um bonco postgres. A configuração padrão de acesso ao banco assume que existe um banco de
{'NAME': 'odp', 'USER': 'postgres', 'PASSWORD': '123456', 'HOST': 'localhost'} portanto certifique-se de haver um banco
com essas especificações ou acesse o arquivo de configução - myproject/settings.py - e ajuste as configurações para
acessar o banco que você deseja. Após verificar essas informações execute as etapas a baixo para por o projeto em execução.

### CRIANDO UMA MIGAÇÃO PARA O SISTEMA
`python manage.py makemigrations`

### APLICANDO A MIGRAÇÃO NO BANCO DE DADOS
`python manage.py migrate`

Agora devemos criar um usuário para acessar a aplicação e gerenciar os demais usuários. Para isso vamos usar o comando
do Django exibido a baixo. Posteriormente podemos criar e gerenciar novos usuários no admin do django acessando
´seu_ip:8000/admin´
- `python manage.py createsuperuser`




Se tudo tiver ocorrido sem erros, agora estamos prontos para inicir nosso servidor e começar a usar a aplicação.
O comando a seguir vai iniciar o servidor no seu ip público na porta 8000

### INICIANDO O SERVIDOR
`python manage.py runserver 0.0.0.0:8000`

Agora basta acessar seu_ip:8000/gestorbases. 