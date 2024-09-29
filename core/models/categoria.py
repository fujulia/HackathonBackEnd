from django.db import models

class Categoria(models.Model):
    class Tipos(models.IntegerChoices):
        PLACA = 1, "Placa Solar"
        INVERSOR = 2, "Inversor"
        CONECTORES = 3, "Conectores"
        CABOS = 4, "Cabos"
        ESTRUTURA = 5, "Estrutura"
        BATERIA = 6, "Bateria"
        KIT = 7, "Kit solar"
        MICROINVERSORES = 8, "Micro Inversores"
    
    nome = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    tipo = models.IntegerField(choices=Tipos.choices, default=Tipos.PLACA )
    
    class Meta:
        abstract = False 
        
    def __str__(self):
        return self.nome
    
# class CategoriaPlacaSolar(Categoria):
#     tipoCelula = models.CharField(max_length=100, blank=True, null=True)
#     potencia = models.IntegerField(blank=True, null=True)
#     eficiencia = models.FloatField(blank=True, null=True)
#     largura = models.DecimalField(max_digits=10, decimal_places=2) 
#     altura = models.DecimalField(max_digits=10, decimal_places=2)
#     peso = models.DecimalField(max_digits=10, decimal_places=2)
#     temperaturaOperacao = models.DecimalField(max_digits=5, decimal_places=2)
#     toleranciaPotencia = models.IntegerField(blank=True, null=True)
    
    
# class CategoriaInversor(Categoria):
#     potencia = models.IntegerField(blank=True, null=True)
#     eficiencia = models.FloatField(blank=True, null=True)
    

# class CategoriaConectores(Categoria):
#     tensaoNominal = models.DecimalField(max_digits=5, decimal_places=2)
#     correnteNominal = models.DecimalField(max_digits=5, decimal_places=2)
#     material = models.CharField(max_length=100, blank=True, null=True)
#     acabamento = models.CharField(max_length=100, blank=True, null=True)
#     comprimento = models.DecimalField(max_digits=10, decimal_places=2)  
#     largura = models.DecimalField(max_digits=10, decimal_places=2)     
#     altura = models.DecimalField(max_digits=10, decimal_places=2)     
#     diametro = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
#     profundidade = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    
    
# class CategoriaCabos(Categoria):
#     material = models.CharField(max_length=100, blank=True, null=True)
#     comprimento = models.DecimalField(max_digits=10, decimal_places=2)  
#     isolamento = models.CharField(max_length=100)
    

# class CategoriaEstrutura(Categoria):
#     largura = models.DecimalField(max_digits=10, decimal_places=2) 
#     altura = models.DecimalField(max_digits=10, decimal_places=2)
#     capacidadeCarga = models.DecimalField(max_digits=10, decimal_places=2)
    

# class CategoriaBateria(Categoria):
#     capacidade = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     tensaoNominal = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
#     vidaUtil = models.IntegerField(default=0, blank=True, null=True)  
    
    
# class CategoriaKitSolar(Categoria):
    
#     class TipoKit(models.IntegerChoices):
#         ONGRID= 1, "On-grid"
#         OFFGRID = 2, "Off-grid"
    
#     tipo = models.IntegerField(choices=TipoKit.choices, default=TipoKit.ONGRID)
#     placa = models.ManyToManyField(CategoriaPlacaSolar, related_name="kit_placa", blank=True )
#     inversor = models.ForeignKey(CategoriaInversor, on_delete=models.PROTECT, related_name="inversor", null=True, blank=True)
#     bateria = models.ForeignKey(CategoriaBateria, on_delete=models.PROTECT, related_name="bateria", null=True, blank=True)