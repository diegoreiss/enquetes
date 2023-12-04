# enquetes

# Primeiros Passos

Clone o repositório do Github e acesse o novo diretório:

    $ git clone git@github.com/diegoreiss/enquetes.git
    $ cd enquetes
    
Ative o ambiente virtual para o seu projeto.

Instale as dependências do projeto:

    $ pip install -r requirements.txt
    
    
Em seguida, aplique as migrações:

    $ python manage.py migrate
    

Agora você pode iniciar o servidor de desenvolvimento:

    $ python manage.py runserver
