from django.urls import path

from . import views

 

urlpatterns = [

  path('', views.index, name='home'),
  path('add-pergunta/', views.add_pergunta, name='add-pergunta'),
  path('resultados/', views.resultados, name='resultados'),
  path('minhas_enquetes/', views.minhas_enquetes, name='minhas_enquetes'),
  path('historico_enquetes/', views.historico_enquetes, name='historico_enquetes'),
  path('add-enquete/<int:id>', views.add_enquete, name='add-enquete'),
  path('desativar-enquete/<int:pergunta_id>/', views.desativar_enquete, name='desativar_enquete'),
  path('resultados_enquete/<int:pergunta_id>/', views.resultados_enquete, name='resultados_enquete'),

]