from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from.models import Pergunta, OpcaoResposta
from django.contrib.auth.decorators import login_required
from random import randint

@login_required(redirect_field_name='login')
def index(request):

  
    return render(request, 'pages/index.html')

def add_pergunta(request ):
  if request.method == 'POST':

    titulo = request.POST.get('name')
    pergunta = request.POST.get('email')
    cod = randint(100, 10000)
    data_criacao = datetime.now()
    active = True

    Pergunta.objects.create(
      
    )
    return redirect('login')
    
  else:
    return render(request,'pages/add-pergunta.html') 