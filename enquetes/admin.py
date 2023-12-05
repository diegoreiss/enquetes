from django.contrib import admin
from.models import Pergunta, OpcaoResposta


class PerguntaAdmin(admin.ModelAdmin):
    list_display=['id','user', 'titulo','active'] 
    #list_filter=['active']
    

class OpcaoRespostaAdmin(admin.ModelAdmin):
    list_display=['pergunta','id'] 
    
  
admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(OpcaoResposta, OpcaoRespostaAdmin )
