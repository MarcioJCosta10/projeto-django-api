# Iniciando o projeto
### como baixamos do site Alura já terá o projeto criado e app startado com os pacotes linstados no requirement 
### criar o repositório no github e efetuar push
### criar e ativar o venv
### criar e realizar as migrações
### criar o superusuario para o admin --python3 manage.py createsuperuser

# --------------------------------------------------
# Iniciar as validações dos campos
### em models.py colocar a tag unique=true para o campo cpf 
### vamos fazer uma analise e comprovar que o Serializer carrega as validações definidas no models
### abrir o shell do python3
### python3 manage.py shell
### realizar o impor da classe ClienteSerializer
### from clientes.serializer import ClienteSerializer
### instanciar em s = ClienteSerializer() 
### >>> s = ClienteSerializer()
### >>> print(repr(s))

``
    ClienteSerializer():
    id = IntegerField(label='ID', read_only=True)
    nome = CharField(max_length=100)
    email = EmailField(max_length=30)
    cpf = CharField(max_length=11, validators=[<UniqueValidator(queryset=Cliente.objects.all())>])
    rg = CharField(max_length=9)
    celular = CharField(max_length=14)
    ativo = BooleanField()
``
### veremos que nosso serializer terá as propriedades dos campos do models 

# Agora vamos incluir as validações direto no serializer e ver as vantagens dessa atitude
### no escopo do Serializer ClienteSerializer criar as função de validação

### colocar as logicas das validações em outro arquivo
### criar o arquivo validator.py 
### em ClienteSerializer criar apenas a função--> def validate(self,data):
### self e a instancia que estou.
### atraves de data vou ter acesso a todos os campos de uma só vez  

### em validator mudar a função validate_cpf

### usar regex para validar o número do telefone
### importar validações por exemplo para cpf:
### em validator instalar --> pip install validate-docbr
### fazero o import from validate_docbr import CPF
### criar uma instância do cpf e inserir na na validação

### usar o scrip para criar pessoas fake e popular o banco de dados
### instalar --> pip install Faker
### rodar o arquivo para popular o banco de dados

# criar uma paginação na api
### acessar django rest pagination
### localizar a configuração padrão de paginação e inserir em settings.py

```python3
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}
```
#  Colocar uma ordenação na API pelo nome dos clientes
### mudar no admin.py adicionar a propriedade ordering
### agora para colocar ordenação na api 
### instalar --> pip install django-filter
### adiconar django-filter nos apps instaled
### mudar na views.py informando que esses valores que ela está mostrando tem uma ordenação
### importar o filters
### importar --> from django_filters.rest_framework import DjangoFilterBackend
### adicinar a proprienda --> filter_backends = [DjangoFilterBackend, filters.OrderingFilter] isso
### diz que temos uma ordenação no backend e essa ordenação vira do filter
### adicionar a propriedade -->  ordering_fields = ['nome']


# adicionar Busca e Filtros na API
# busca:
### como já instalamos o filter basta adicionar a linha de configuração(campo) na classe
###     filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
###    search_fields = ['nome', 'email', 'cpf']
### adicionar um filtro para ativos e inativos
### incluir o campo --> filterset_fields = ['ativo']

# iniciar o deploy
### Vamos fazer no heroku Cadastro no heroku ##Nm12345678
### criar app no heroku
### acessar para instruções: https://www.heroku.com/python
### requisitos: https://devcenter.heroku.com/articles/getting-started-with-python

### instalar o CLI(linha de comados) do heroku --> linha 
'''
sudo snap install heroku --classic
'''
# dentro do app --> new terminal 
### heroku login digitar qualquer letra na confirmação e confirmar op login
### 

# agora preparar o django para o deploy
# pip install django-heroku 
# psycopg2
# psycopg2-binary

# erros precisa estar com o banco no postgres
# sudo apt-get install libpq-dev --> caso de erro no pip install psycopg2

# em settings.py 
### import django_heroku
### no fim da pagina --> django_heroku.settings(locals())

### instalar o gunicorn --> É uma interface de comunicação entre servidores web
## pip install gunicorn==20.0.4

# indicar que essa aplicação será executada com base no guincorn
### criar o arquivo Procfile e inserir --> web: gunicorn setup.wsgi

### iniciar o repositorio github
### git init caso não exista
### git add .
### git commit -m "deploy of projects clientes"
### heroku git:remote -a drf-django-clientes


# mandar para o heroku -->$ heroku git:remote -a drf-django-clientes
# git add .
# git commit -am "make it better in heroku"
# git push heroku master

