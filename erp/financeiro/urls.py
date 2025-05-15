from django.urls import path
from . import views

urlpatterns = [
    path('', views.exibir_tela_inicial),
    path('contas/pagar', views.listar_contas_a_pagar),
    path('contas/pagar/registrar', views.registrar_contas_a_pagar),
    path('contas/pagar/editar/<int:id>', views.editar_contas_a_pagar),
    path('contas/pagar/excluir/<int:id>', views.excluir_contas_a_pagar),
    path('contas/receber', views.listar_contas_a_receber),
    path('contas/receber/registrar', views.registrar_contas_a_receber),
    path('contas/receber/editar/<int:id>', views.editar_contas_a_receber),
    path('contas/receber/excluir/<int:id>', views.excluir_contas_a_receber),
]