from django.db import models
from django.contrib.auth.models import User

class Pergunta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    pergunta = models.CharField(max_length=255)
    cod = models.IntegerField(unique=True)
    data_criacao = models.DateTimeField()
    data_encerramento = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField(default=False)
    

    def __str__(self):
        return f'{self.titulo} - {self.pergunta}'
    
    class Meta:
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'

class OpcaoResposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_opcao = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.pergunta} - {self.texto_opcao}'

    class Meta:
        verbose_name = 'Opção de Resposta'
        verbose_name_plural = 'Opções de Resposta'

class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    opcao_escolhida = models.ForeignKey(OpcaoResposta, on_delete=models.CASCADE)
    data_resposta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Resposta de {self.usuario} para {self.pergunta}. Respondeu: {self.opcao_escolhida.texto_opcao}'

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'