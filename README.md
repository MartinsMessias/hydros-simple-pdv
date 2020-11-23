# Hydros SimplePDV - Desafio03
#### Sistema de PDV simples [EM CONSTRUÇÃO].


## Como executar 
##### Ambiente de desenvolvimento testado no [Ubuntu 20.04]*
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