from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import ContaPagar, ContaReceber
from rest_framework import viewsets, permissions
from .serializers import ContaPagarSerializer, ContaReceberSerializer
from .utils import moeda_para_float
import requests

# Create your views here.

class ContaPagarViewSet(viewsets.ModelViewSet):
    queryset = ContaPagar.objects.all()
    serializer_class = ContaPagarSerializer
    permission_classes = [permissions.AllowAny]

class ContaReceberViewSet(viewsets.ModelViewSet):
    queryset = ContaReceber.objects.all()
    serializer_class = ContaReceberSerializer
    permission_classes = [permissions.AllowAny]

def exibir_tela_inicial(request):
    return render(request, "financeiro_index.html")

def listar_contas_a_pagar(request):
    contas_a_pagar = ContaPagar.objects.all()
    return render(request, "listar_contas_a_pagar.html", {"contas_a_pagar": contas_a_pagar})

def listar_contas_a_receber(request):
    contas_a_receber = ContaReceber.objects.all()
    return render(request, "listar_contas_a_receber.html", {"contas_a_receber": contas_a_receber})

def registrar_contas_a_pagar(request):
    if (request.method == "POST"):
        conta_a_pagar = ContaPagar()

        conta_a_pagar.codigo_fornecedor = request.POST.get("fornecedor")
        conta_a_pagar.descricao = request.POST.get("descricao")
        conta_a_pagar.valor = moeda_para_float(request.POST.get("valor"))
        conta_a_pagar.vencimento = datetime.strptime(request.POST.get("vencimento"), "%Y-%m-%d").date()
        conta_a_pagar.status = request.POST.get("status")

        conta_a_pagar.save()
        return HttpResponseRedirect("/financeiro/contas/pagar")

    fornecedores = _obter_fornecedores()
    return render(request, "registrar_contas_a_pagar.html", {"fornecedores": fornecedores})

def registrar_contas_a_receber(request):
    if (request.method == "POST"):
        conta_a_receber = ContaReceber()

        conta_a_receber.codigo_cliente = request.POST.get("cliente")
        conta_a_receber.descricao = request.POST.get("descricao")
        conta_a_receber.valor = moeda_para_float(request.POST.get("valor"))
        conta_a_receber.data_prevista = datetime.strptime(request.POST.get("data-prevista"), "%Y-%m-%d").date()
        conta_a_receber.status = request.POST.get("status")

        conta_a_receber.save()
        return HttpResponseRedirect("/financeiro/contas/receber")

    clientes = _obter_clientes()
    return render(request, "registrar_contas_a_receber.html", {"clientes": clientes})

def editar_contas_a_pagar(request, id):
    conta_a_pagar = ContaPagar.objects.get(id=id)

    if (request.method == "POST"):
        conta_a_pagar.codigo_fornecedor = request.POST.get("fornecedor")
        conta_a_pagar.descricao = request.POST.get("descricao")
        conta_a_pagar.valor = moeda_para_float(request.POST.get("valor"))
        conta_a_pagar.vencimento = datetime.strptime(request.POST.get("vencimento"), "%Y-%m-%d").date()
        conta_a_pagar.status = request.POST.get("status")

        conta_a_pagar.save()
        return HttpResponseRedirect("/financeiro/contas/pagar")
    
    fornecedores = _obter_fornecedores()
    return render(request, "editar_contas_a_pagar.html", {"conta_a_pagar": conta_a_pagar, "fornecedores": fornecedores})

def editar_contas_a_receber(request, id):
    conta_a_receber = ContaReceber.objects.get(id=id)

    if (request.method == "POST"):
        conta_a_receber.codigo_cliente = request.POST.get("cliente")
        conta_a_receber.descricao = request.POST.get("descricao")
        conta_a_receber.valor = moeda_para_float(request.POST.get("valor"))
        conta_a_receber.data_prevista = datetime.strptime(request.POST.get("data-prevista"), "%Y-%m-%d").date()
        conta_a_receber.status = request.POST.get("status")

        conta_a_receber.save()
        return HttpResponseRedirect("/financeiro/contas/receber")
    
    clientes = _obter_clientes()
    return render(request, "editar_contas_a_receber.html", {"conta_a_receber": conta_a_receber, "clientes": clientes})

def excluir_contas_a_pagar(request, id):
    conta_a_pagar = ContaPagar.objects.get(id=id)

    if (request.method == "POST"):
        conta_a_pagar.delete()
        return HttpResponseRedirect("/financeiro/contas/pagar")
    
    return render(request, "excluir_contas_a_pagar.html", {"conta_a_pagar": conta_a_pagar})

def excluir_contas_a_receber(request, id):
    conta_a_receber = ContaReceber.objects.get(id=id)

    if (request.method == "POST"):
        conta_a_receber.delete()
        return HttpResponseRedirect("/financeiro/contas/receber")
    
    return render(request, "excluir_contas_a_receber.html", {"conta_a_receber": conta_a_receber})

def _obter_clientes():
    response = requests.get("https://macielbrabo.pythonanywhere.com/clientes/clientes/")
    return response.json()

def _obter_fornecedores():
    response = requests.get("https://habini86.pythonanywhere.com/fornecedor/fornecedores", 
                            auth=("admin", "12345"))
    return response.json()