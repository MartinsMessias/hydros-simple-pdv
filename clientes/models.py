from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=250, blank=False, null=False)
    cpf_cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return f'{self.nome} - {self.cpf_cnpj}'