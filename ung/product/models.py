from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
