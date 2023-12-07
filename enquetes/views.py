from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from.models import Pergunta, OpcaoResposta, Resposta
from django.contrib.auth.decorators import login_required
from random import randint
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.db import transaction

from utils import email_utils


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
@transaction.atomic
def add_pergunta(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        pergunta_texto = request.POST.get('pergunta')
        opcoes_resposta = request.POST.getlist('opcao_resposta')
        
        nova_pergunta = Pergunta.objects.create(
            user=request.user, 
            titulo=titulo,
            pergunta=pergunta_texto,
            cod=randint(100, 10000),
            data_criacao=datetime.now(),
            active=True,
        )
        
        for opcao_texto in opcoes_resposta:
            OpcaoResposta.objects.create(
                pergunta=nova_pergunta,
                texto_opcao=opcao_texto
            )

        return redirect('home')
    else:
        return render(request, 'pages/add-pergunta.html')


@login_required
@transaction.atomic
def desativar_enquete(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    pergunta.data_encerramento = datetime.now()

    resultados = Resposta.objects.filter(pergunta=pergunta) 
    ranking = resultados.values('opcao_escolhida__texto_opcao') \
        .annotate(total=Count('opcao_escolhida')) \
        .order_by('-total')
    
    if not ranking:
        return redirect('minhas_enquetes')

    mais_votado = max(ranking, key=lambda opcao: opcao['total'])
    
    ranking_text = f'A Enquete com o título {pergunta.titulo}, ' + \
        f'com a pergunta {pergunta.pergunta} foi encerrada...\n\n' + \
        'Os resultados foram:\n\n'
    ranking_text += '\n'.join(f'{opcao["opcao_escolhida__texto_opcao"]} com {opcao["total"]} votos.' for opcao in ranking)
    ranking_text += f'\n\nO mais votado foi o {mais_votado["opcao_escolhida__texto_opcao"]} com {mais_votado["total"]} votos.'

    pergunta.active = False
    pergunta.save()

    emails = resultados.values_list('usuario__email').distinct()
    for email in emails: email_utils.send_email('Enquete Encerrada', email, ranking_text)
    
    return redirect('minhas_enquetes') 


@login_required(redirect_field_name='login')
@transaction.atomic
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