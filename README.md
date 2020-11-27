# Hydros SimplePDV - Desafio03
#### Sistema de PDV simples [EM CONSTRUÇÃO].


## Como executar 
##### Instalar dependencias do WeasyPrint
https://weasyprint.readthedocs.io/en/stable/install.html
##### Ambiente de desenvolvimento testado no [Ubuntu 20.04 - Python3.8]*
``` bash
$ git clone https://github.com/MartinsMessias/hydros-simple-pdv.git
$ cd hydros-simple-pdv/
$ source env/bin/activate
$ pip install -r requirements.txt
```

### Migrações
``` bash
$ python manage.py migrate --run-syncdb
```

### Criando usuário administrador
#### Com ele vai poder adicionar os logins de funcionários

``` bash
$ python manage.py createsuperuser
```
Usuário admin do banco de dados de exemplo [example-db.sqlite3]:
 
Usuário: admin
Senha: admin

### Rodar

``` bash
$ python manage.py runserver [porta]
```

### Requisitos identificados

 -  Tela de venda 
    - Data - OK
    - Cliente - OK
    - Forma de Pagamento (Dinheiro, Cartão) - OK
    - Items da compra - EM CONSTRUÇÃO
    - Somar total da compra - EM CONSTRUÇÃO
     
 -  Imprimir via da venda - OK
    - Baixar dados da venda em PDF

 -  CRUD de Produtos - OK
 
 -  CRUD de Usuários - OK
    - Cadastro
    - Autenticação
 
 -  CRUD de Clientes - OK
    - Opção de listar compras realizadas - OK
