from django.db import models

class Telefone(models.Model):
    ddd = models.CharField(max_length=3, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    
    def __str__(self):
       return f'({self.ddd}) {self.numero}'
  