# Hydros SimplePDV - Desafio03
#### Sistema de PDV simples [EM CONSTRUÇÃO].


## Como executar 
##### Ambiente de desenvolvimento testado no [Ubuntu 20.04 - Python3.8]*
``` bash
$ git clone https://github.com/MartinsMessias/hydros-simple-pdv.git
$ cd hydros-simple-pdv/
$ source env/bin/activate
$ pip install -r requirements.txt
```

### Migrações
``` bash
$ python manage.py migrate
```

### Criando usuário administrador
#### Com ele vai poder adicionar os logins de funcionários

``` bash
$ python manage.py createsuperuser
```

### Rodar

``` bash
$ python manage.py runserver [porta]
```

### Requisitos identificados

 -  Tela de venda - EM CONSTRUÇÃO
    - Data
    - Cliente
    - Forma de Pagamento (Dinheiro, Cartão)
    - Items da compra
    - Somar total da compra
     
 -  Imprimir via da venda - OK
    - Baixar dados da venda em PDF

 -  CRUD de Produtos - OK
 
 -  CRUD de Usuários - OK
    - Cadastro
    - Autenticação
 
 -  CRUD de Clientes - OK
    - Opção de listar compras realizadas - EM CONSTRUÇÃO