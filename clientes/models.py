from venv import create
from django.db import models
from datetime import datetime

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30, )
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9)
    celular = models.CharField(max_length=14)
    ativo = models.BooleanField()
    created = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.nome
