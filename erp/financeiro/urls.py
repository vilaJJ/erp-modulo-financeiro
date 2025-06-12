from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ContaPagarViewSet, ContaReceberViewSet
from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r'contas-pagar', ContaPagarViewSet)
router.register(r'contas-receber', ContaReceberViewSet)

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

urlpatterns += router.urls