from django.contrib import admin
from .models import Pergunta, OpcaoResposta, Resposta


class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'titulo','active') 
    list_display_links = ('id', 'user')
    list_filter = ('active', )

    search_fields = (
        'user__username',
    )


class RespostaAdmin(admin.ModelAdmin):
    list_display = ('id', 'pergunta')
    

class OpcaoRespostaAdmin(admin.ModelAdmin):
    list_display = ('id', 'pergunta')
    
  
admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(OpcaoResposta, OpcaoRespostaAdmin)
admin.site.register(Resposta, RespostaAdmin)
