# Catalogo---Backend

Olá.
Para utilizar o sistema backend, teremos que realizar algumas configurações antes.


CONFIGURACOES BASICAS:

  Para rodar o servidor python, execute o comando: python manage.py runserver no terminal;
  Para acessar o painel administrativo, execute o comando: python manage.py createsuperuser

-------------------------------------------------------------------------------------------------------------------------------------------------------------
BANCO DE DADOS:

Para este exemplo, utilizei o XAMPP como servidor para rodar o banco de dados MYSQL.

Para configurar o MYSQL com o Django é necessário: 

  - Instalar o mysql pelo pip -> pip install pymysql
  - Instalar o mysqlclient -> pip install mysqlclient

  - Fazer a ligação e a configuração no arquivo config/settings.py para configurar com o mysql

  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'catalogo',
          'USER': 'root',
          'PASSWORD': '',
          'HOST': 'localhost',
          'PORT': '3306',
      }
  }
  
  Depois de feitos os processos acima, temos que instanciar nossa aplicação no INSTALLED_APPS dos Settings
  
  INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalogo',
]
  
  Para setar em migrations a construção feita no model, utilize o comando: python manage.py makemigrations catalogo
  
  Logo em seguida, execute o comando: python manage.py migrate para o django colocar as alterações no seu banco de dados e disponibilizar no admin do django.
  
  
  -------------------------------------------------------------------------------------------------------------------------------------------------------------
  REST FRAMEWORK
  
  Para instalar o rest_framework do django, utilize o comando: pip install djangorestframework
  
  
  
  
  -------------------------------------------------------------------------------------------------------------------------------------------------------------
  
  
  SOBRE O CORS
  
  Para permitir conexões via HTTP foi necessário realizar uma mudança nos Settings. 
  Foram adicionadas as seguintes informações:
  
  CORS_ORIGIN_ALLOW_ALL = True
  
  MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    '...,
    
]

INSTALLED_APPS = [
    ...,
    'catalogo',
    'rest_framework',
    'corsheaders'
]


Depois de feitas as alterações, você conseguirá acessar da sua aplicação frontend.

-------------------------------------------------------------------------------------------------------------------------------------------------------------

SOBRE O FUNCIONAMENTO


O Backend em questão, serve basicamente para receber as requisições e realizar as buscas de acordo com os parâmetros e requisições desejados.

O arquivo Models, é o modelo dos parâmetros e dados de cada uma das tabelas existentes no banco de dados.
O Serializer, é o serializador dos modelos criados, indicando os campos e a tabela desejada em cada uma das classes declaradas.
O arquivo Views, é o arquivo onde configuro os viewSets e funciona como se fosse uma query do SQL convencional, onde consigo criar os filtros que porventura quiser
realizar para as buscas.

O arquivo urls.py da pasta config, é onde defino minhas rotas para todas as requisições que vierem ao meu backend e para o painel de admin do django.


-------------------------------------------------------------------------------------------------------------------------------------------------------------


#QUALQUER DÚVIDA FICO A DISPOSIÇÃO
  
  
  



  
  
  
