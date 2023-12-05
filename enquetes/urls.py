from django.urls import path

from . import views

 

urlpatterns = [

  path('', views.index, name='home'),
  path('add-pergunta/', views.add_pergunta, name='add-pergunta')

]