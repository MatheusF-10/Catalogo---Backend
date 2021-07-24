from django.db import models


class Modulo(models.Model):
    nome = models.CharField(max_length=200)
    num_aulas = models.IntegerField(null=True)

    def __str__(self):
        return self.nome


class Aula(models.Model):
    nome = models.CharField(max_length=200)
    fk_modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    data_aula = models.DateField('data da aula')

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    rg = models.CharField(max_length=9)

    def __str__(self):
        return self.nome
