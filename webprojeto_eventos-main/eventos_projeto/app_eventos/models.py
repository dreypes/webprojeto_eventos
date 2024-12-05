#from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Classe Local
class Local(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.TextField()

    def __str__(self):
        return self.nome

# Classe Evento
class Evento(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateTimeField()
    local = models.CharField(max_length=255, verbose_name="Local do Evento")
    descricao = models.TextField()

    def __str__(self):
        return self.nome

# Classe Usuario (extendendo a funcionalidade do User)
class Usuario(models.Model):
    usuario = models.CharField(max_length=50, unique=True)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.usuario.username

# Classe Convite
class Convite(models.Model):
    PENDENTE = 'pendente'
    ACEITO = 'aceito'
    RECUSADO = 'recusado'

    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (ACEITO, 'Aceito'),
        (RECUSADO, 'Recusado'),
    ]

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    convidado = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Usando Usuario em vez de User
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDENTE)

    def __str__(self):
        return f"Convite para {self.convidado} no evento {self.evento}"

