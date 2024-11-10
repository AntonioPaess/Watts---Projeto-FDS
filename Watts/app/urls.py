from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
    path('addLocacao/', AddLocacao.as_view(), name='addLocacao'),
    path('deleteLocacao/<int:locacao_id>/', DeleteLocacao.as_view(), name='deleteLocacao'),
    path('addComodo/', CriarComodo.as_view(), name='addComodo'),
    path('deleteComodo/<int:comodo_id>/', DeleteComodo.as_view(), name='deleteComodo'),
    path('addPontodeenergia/', CriarPontoDeEnergia.as_view(), name='addPontodeenergia'),
    path('deletePontodeenergia/<int:pontodeenergia_id>/', DeletePontodeenergia.as_view(), name='deletePontodeenergia'),
    path('calcular_custo/<int:pontodeenergia_id>/<int:horas>/', CalcularCustoPontoDeEnergia.as_view(), name='calcular_custo'),
    path('calcular_custo_comodo/<int:comodo_id>/', CalcularCustoComodo.as_view(), name='calcular_custo_comodo'),
    path('calcular_custo_locacao/<int:locacao_id>/', CalcularCustoLocacao.as_view(), name='calcular_custo_locacao'),
]