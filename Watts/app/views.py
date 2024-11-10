from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from django.views import View
from .models import Locacao, Comodo, Pontodeenergia

class HomeViews(View):
    def get(self, request):
        pontosdeenergia = Pontodeenergia.objects.all()
        locacoes = Locacao.objects.all()
        comodos = Comodo.objects.all()
        return render(request, 'home.html', {
            'pontosdeenergia': pontosdeenergia,
            'locacoes': locacoes,
            'comodos': comodos
        })

class AddLocacao(View):
    def get(self, request):
        return render(request, 'AddLocacao.html')

    def post(self, request):
        name = request.POST.get("nome")
        state = request.POST.get("estado")

        errors = {}
        if not name:
            errors['name_error'] = 'O campo nome é obrigatório'
        if not state:
            errors['state_error'] = 'O campo estado é obrigatório'

        if errors:
            return render(request, 'AddLocacao.html', errors)

        locacao = Locacao(
            nome=name,
            estado=state
        )
        locacao.save()
        return redirect('home')

class DeleteLocacao(View):
    def post(self, request, locacao_id):
        locacao = get_object_or_404(Locacao, id=locacao_id)
        locacao.delete()
        return redirect('home')

class CriarComodo(View):
    def get(self, request):
        locacoes = Locacao.objects.all()
        return render(request, 'AddComodo.html', {'locacoes': locacoes})

    def post(self, request):
        locacao_id = request.POST.get('locacao')
        nome_comodo = request.POST.get('nome')

        if not nome_comodo:
            locacoes = Locacao.objects.all()
            return render(request, 'AddComodo.html', {'locacoes': locacoes, 'error_message': 'O campo nome é obrigatório'})

        if not locacao_id:
            locacoes = Locacao.objects.all()
            return render(request, 'AddComodo.html', {'locacoes': locacoes, 'error_message': 'O campo locação é obrigatório'})

        try:
            locacao = Locacao.objects.get(id=locacao_id)
            Comodo.objects.create(locacao=locacao, nome=nome_comodo)
            return redirect('home')  # Redirecionar após sucesso
        except Locacao.DoesNotExist:
            # Se a locação não for encontrada, exiba uma mensagem de erro
            locacoes = Locacao.objects.all()
            return render(request, 'AddComodo.html', {'locacoes': locacoes, 'error_message': 'Locação inválida!'})

class DeleteComodo(View):
    def post(self, request, comodo_id):
        comodo = get_object_or_404(Comodo, id=comodo_id)
        comodo.delete()
        return redirect('home')

class CriarPontoDeEnergia(View):
    def get(self, request):
        locacoes = Locacao.objects.all()
        comodos = Comodo.objects.all()
        return render(request, 'AddPontoDeEnergia.html', {'locacoes': locacoes, 'comodos': comodos})

    def post(self, request):
        locacao_id = request.POST.get('locacao')
        comodo_id = request.POST.get('comodo')
        nome = request.POST.get('nome')
        gastos = request.POST.get('gastos')
        quantidade = request.POST.get('quantidade')

        if not nome:
            locacoes = Locacao.objects.all()
            comodos = Comodo.objects.all()
            return render(request, 'AddPontoDeEnergia.html', {'locacoes': locacoes, 'comodos': comodos, 'error_message': 'O campo nome é obrigatório'})
        if not gastos:
            locacoes = Locacao.objects.all()
            comodos = Comodo.objects.all()
            return render(request, 'AddPontoDeEnergia.html', {'locacoes': locacoes, 'comodos': comodos, 'error_message': 'O campo gastos é obrigatório'})
        if not quantidade:
            locacoes = Locacao.objects.all()
            comodos = Comodo.objects.all()
            return render(request, 'AddPontoDeEnergia.html', {'locacoes': locacoes, 'comodos': comodos, 'error_message': 'O campo quantidade é obrigatório'})

        try:
            gastos = float(gastos)
            if gastos < 0:
                raise ValueError('Gastos negativos')
        except ValueError:
            locacoes = Locacao.objects.all()
            comodos = Comodo.objects.all()
            return render(request, 'AddPontoDeEnergia.html', {'locacoes': locacoes, 'comodos': comodos, 'error_message': 'O campo gastos não pode ser negativo'})

        try:
            quantidade = int(quantidade)
            if quantidade < 0:
                raise ValueError('Quantidade negativa')
        except ValueError:
            locacoes = Locacao.objects.all()
            comodos = Comodo.objects.all()
            return render(request, 'AddPontoDeEnergia.html', {'locacoes': locacoes, 'comodos': comodos, 'error_message': 'O campo quantidade não pode ser negativo'})

        try:
            locacao = Locacao.objects.get(id=locacao_id)
            comodo = Comodo.objects.get(id=comodo_id)
            if comodo.locacao != locacao:
                raise ValueError('Cômodo não pertence à locação')
            Pontodeenergia.objects.create(locacao=locacao, comodo=comodo, nome=nome, gastos=gastos, quantidade=quantidade)
            return redirect('/')  # Redirecionar após sucesso
        except (Locacao.DoesNotExist, Comodo.DoesNotExist):
            locacoes = Locacao.objects.all()
            comodos = Comodo.objects.all()
            return render(request, 'AddPontoDeEnergia.html', {'locacoes': locacoes, 'comodos': comodos, 'error_message': 'Locação ou cômodo inválido!'})
        except ValueError as e:
            locacoes = Locacao.objects.all()
            comodos = Comodo.objects.all()
            return render(request, 'AddPontoDeEnergia.html', {'locacoes': locacoes, 'comodos': comodos, 'error_message': str(e)})

class DeletePontodeenergia(View):
    def post(self, request, pontodeenergia_id):
        pontodeenergia = get_object_or_404(Pontodeenergia, id=pontodeenergia_id)
        pontodeenergia.delete()
        return redirect('home')

class CalcularCustoPontoDeEnergia(View):
    def get(self, request, pontodeenergia_id, horas):
        ponto = get_object_or_404(Pontodeenergia, id=pontodeenergia_id)
        try:
            horas = int(horas)
        except ValueError:
            horas = 1
        custo = ponto.calcular_custo(horas)
        data = {
            'ponto': {
                'nome': ponto.nome,
                'gastos': str(ponto.gastos),
                'quantidade': ponto.quantidade,
                'comodo': ponto.comodo.nome,
                'locacao': ponto.locacao.nome,
            },
            'horas': horas,
            'custo': str(custo),
        }
        return JsonResponse(data)

class CalcularCustoComodo(View):
    def get(self, request, comodo_id):
        comodo = get_object_or_404(Comodo, id=comodo_id)
        horas = request.GET.get('horas', 1)
        try:
            horas = int(horas)
        except ValueError:
            horas = 1

        pontos = Pontodeenergia.objects.filter(comodo=comodo)
        custo_total = sum(ponto.calcular_custo(horas) for ponto in pontos)

        return JsonResponse({
            'comodo': comodo.nome,
            'horas': horas,
            'custo': str(custo_total)
        })

class CalcularCustoLocacao(View):
    def get(self, request, locacao_id):
        locacao = get_object_or_404(Locacao, id=locacao_id)
        horas = request.GET.get('horas', 1)
        try:
            horas = int(horas)
        except ValueError:
            horas = 1

        custo_total = locacao.calcular_custo(horas)

        return JsonResponse({
            'locacao': locacao.nome,
            'horas': horas,
            'custo': str(custo_total)
        })