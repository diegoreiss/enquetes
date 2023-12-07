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


variáveis de ambiente do arquivo .env (Lembre-se de criar o arquivo):
    
    EMAIL_SENDER_SMTP_SSL=
    EMAIL_SENDER_NAME=
    EMAIL_SENDER_PASSWORD=
    EMAIL_SENDER_PORT=
    EMAIL_SENDER_SMTP_SSL=