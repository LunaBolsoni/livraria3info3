from django.db import models

class autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True) 

    def __str__(self):
        return f'{self.nome} - {self.email}'
    
