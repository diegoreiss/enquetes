from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def index(request):

  
    return render(request, 'pages/index.html')