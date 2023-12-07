from django.shortcuts import render, HttpResponse,redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from random import randint

def user_login(request):

    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')

        userVerify = auth.authenticate(
            request, username=user, password=password)
        
        if userVerify == None:
            messages.info(request, 'Usuário ou senha incorretos seu tanso!')
            return redirect('login')
        else:
            auth.login(request, userVerify)
            return redirect('home')
    else:

        return render(request,'pages/login.html')

from django.contrib import messages

def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senhaconfirma = request.POST.get('senha-repete')
        is_active = True

        if not (name and usuario and email and senha and senhaconfirma):
            messages.error(request, 'Por favor, preencha todos os campos.')
            return render(request, 'pages/add-user.html')

        if senha != senhaconfirma:
            messages.error(request, 'As senhas não correspondem.')
            return render(request, 'pages/add-user.html')

        user = User.objects.create_user(
            username=usuario, email=email,
            password=senha, first_name=name, is_active=is_active
        )
        if user:
            messages.success(request, 'Cadastro concluído com sucesso.', extra_tags='success')
            return redirect('login')
        else:
            messages.error(request, 'Ocorreu um erro ao criar o usuário.')
            return render(request, 'pages/add-user.html')

    else:
        return render(request, 'pages/add-user.html')

def logout(request):
  auth.logout(request)
  return redirect('login') 
 
    