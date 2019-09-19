# Monitor de Temperatura

Solução para monitoramento da variação de temperatura de cidades.

## Dependências

* Python 3.7.3
* Pipenv

## Instalação e execução em um ambiente local

    $ pipenv install --three
    $ pipenv shell
    $ python manage.py migrate
    $ python manage.py runserver
    
## Subindo o celery

    $ celery -A monitor beat (Execute em outra janela do terminal)

## Fazendo chamadas ao celery

    $ celery -A monitor worker -l info (Execute em outra janela do terminal)


Na máquina local acesse http://localhost:8000/city/

That's all
