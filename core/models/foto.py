from django.db import models
from .user import User

class Foto(models.Model):
    imagem_url = models.URLField(max_length=200, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="foto", blank=False, null=False)