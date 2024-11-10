from django.db import models
from decimal import Decimal, ROUND_HALF_UP

COST_PER_KWH = Decimal('0.257')  # Defina o custo por kWh como Decimal

class Locacao(models.Model):
    estado = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)

    def calcular_custo(self, horas):
        comodos = self.comodo_set.all()
        custo_total = Decimal('0.00')
        for comodo in comodos:
            pontos = comodo.pontodeenergia_set.all()
            for ponto in pontos:
                custo_total += ponto.calcular_custo(horas)
        return custo_total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

class Comodo(models.Model):
    locacao = models.ForeignKey(Locacao, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

class Pontodeenergia(models.Model):
    locacao = models.ForeignKey(Locacao, on_delete=models.CASCADE)
    comodo = models.ForeignKey(Comodo, on_delete=models.CASCADE)
    gastos = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantidade = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=100)

    def calcular_custo(self, horas):
        quantidade = self.quantidade if self.quantidade else 1
        custo = self.gastos * Decimal(horas) * COST_PER_KWH * quantidade
        return custo.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
