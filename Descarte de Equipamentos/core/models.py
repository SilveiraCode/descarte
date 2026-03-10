from django.db import models
from django.contrib.auth.models import User

# Lista global para padronizar os resíduos em todo o sistema, atualmente mocados, por ser poucas opções 
TIPOS_RESIDUO = [
    ('ELETRONICOS', 'Eletrônicos (TV, Baterias, etc)'),
    ('VOLUMOSOS', 'Móveis Volumosos (Sofá, Armários)'),
    ('RECICLAVEIS', 'Papel, Plástico, Vidro e Metal'),
    ('OLEO', 'Óleo de Cozinha Usado'),
    ('PODA', 'Restos de Poda / Jardim'),
]

class CategoriaResiduo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    def __str__(self): return self.nome

class SolicitacaoColeta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=100, choices=TIPOS_RESIDUO)
    descricao = models.TextField()
    cep = models.CharField(max_length=9, null=True, blank=True)
    bairro = models.CharField(max_length=100)
    rua = models.CharField(max_length=200)
    endereco_numero = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='solicitacoes/', null=True, blank=True)
    status = models.CharField(max_length=20, default='Pendente')
    data_criacao = models.DateTimeField(auto_now_add=True)

class PontoColeta(models.Model):
    nome = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100, default='Centro')
    rua = models.CharField(max_length=200, null=True, blank=True)
    endereco_numero = models.CharField(max_length=10, null=True, blank=True)
    tipo_residuo = models.CharField(max_length=100, choices=TIPOS_RESIDUO)
    latitude = models.FloatField(default=-26.3725)
    longitude = models.FloatField(default=-48.7210)

    def __str__(self):
        return f"{self.nome} ({self.bairro})"