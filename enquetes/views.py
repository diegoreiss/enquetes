from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from.models import Pergunta, OpcaoResposta, Resposta
from django.contrib.auth.decorators import login_required
from random import randint
from django.shortcuts import get_object_or_404
from django.db.models import Count

def index(request):
    perguntas = Pergunta.objects.filter(active=True)
    if request.user.is_authenticated:
        perguntas = perguntas.exclude(user=request.user)
    return render(request, 'pages/index.html', {'perguntas': perguntas})

@login_required(redirect_field_name='login')
def minhas_enquetes(request):
    perguntas = Pergunta.objects.filter(active=True, user=request.user)
    return render(request, 'pages/minhas_enquetes.html', {'perguntas': perguntas})

@login_required(redirect_field_name='login')
def historico_enquetes(request):
    perguntas = Pergunta.objects.filter(active=False, user=request.user)
    return render(request, 'pages/hitorico_enquetes.html', {'perguntas': perguntas})

@login_required(redirect_field_name='login')
def add_pergunta(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        pergunta_texto = request.POST.get('pergunta')
        opcoes_resposta = request.POST.getlist('opcao_resposta')
        
        # Criação da pergunta
        nova_pergunta = Pergunta.objects.create(
            user=request.user,  # ou defina o usuário de alguma maneira
            titulo=titulo,
            pergunta=pergunta_texto,
            cod=randint(100, 10000),
            data_criacao=datetime.now(),
            active=True,
            total_respostas=0
        )
        
        # Adicionar opções de resposta à pergunta criada
        for opcao_texto in opcoes_resposta:
            OpcaoResposta.objects.create(
                pergunta=nova_pergunta,
                texto_opcao=opcao_texto
            )

        return redirect('home')
    else:
        return render(request, 'pages/add-pergunta.html')
    
def desativar_enquete(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    
    # Define a data de encerramento como o momento atual
    pergunta.data_encerramento = datetime.now()
    pergunta.active = False
    
    # Obtém todas as respostas para esta pergunta
    respostas = Resposta.objects.filter(pergunta=pergunta)
    
    # Calcula o número de respostas para cada opção de resposta
    resultados = respostas.values('opcao_escolhida').annotate(total=Count('opcao_escolhida'))
    
    # Atualiza o campo 'resultado' da pergunta com os resultados calculados
    # Aqui, você pode adaptar a lógica para calcular o resultado da forma desejada
    resultado_final = 0
    for resultado in resultados:
        resultado_final += resultado['total']
    
    pergunta.resultado = resultado_final
    pergunta.save()
    
    return redirect('minhas_enquetes') 


@login_required(redirect_field_name='login')
def add_enquete(request, id):
    pergunta = get_object_or_404(Pergunta, pk=id)
    
    if request.user == pergunta.user:
        return render(request, 'pages/mensagem.html', {'mensagem': 'Você não pode responder sua própria pergunta.'})
    
    opcoes = OpcaoResposta.objects.filter(pergunta=pergunta)

    if request.method == 'POST':
        opcao_escolhida_id = request.POST.get('opcao_escolhida')
        opcao_escolhida = get_object_or_404(OpcaoResposta, pk=opcao_escolhida_id)

        Resposta.objects.create(
            pergunta=pergunta,
            usuario=request.user,
            opcao_escolhida=opcao_escolhida
        )

        
        pergunta.total_respostas += 1
        pergunta.save()

        return redirect('home')  
    
    return render(request, 'pages/add-enquete.html', {'pergunta': pergunta, 'opcoes': opcoes})

def resultados(request):
    perguntas = Pergunta.objects.filter(active=False)
    if request.user.is_authenticated:
        perguntas = perguntas.exclude(user=request.user)
    return render(request, 'pages/resultados.html', {'perguntas': perguntas})

def resultados_enquete(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, 'pages/resultados_enquete.html', {'pergunta': pergunta})