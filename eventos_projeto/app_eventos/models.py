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
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    descricao = models.TextField()
    criador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventos_criados')

    def __str__(self):
        return self.nome

# Classe Usuario (extendendo a funcionalidade do User)
class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.usuario.username

# Classe Convite
class Convite(models.Model):
    STATUS_CONVITE = [
        ('Pendente', 'Pendente'),
        ('Aceito', 'Aceito'),
        ('Recusado', 'Recusado'),
    ]

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='convites')
    convidado = models.ForeignKey(User, on_delete=models.CASCADE, related_name='convites_recebidos')
    status = models.CharField(max_length=10, choices=STATUS_CONVITE, default='Pendente')

    def __str__(self):
        return f"{self.convidado.username} - {self.evento.nome}"

