from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return f'{self.nome} - {self.email}'

    class Meta:
        verbose_name_plural = "autores"
