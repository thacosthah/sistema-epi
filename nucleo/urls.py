from django.urls import path
from . import views

app_name = 'nucleo'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # Colaboradores
    path('colaboradores/', views.lista_colaboradores, name='lista_colaboradores'),
    path('colaboradores/novo/', views.cadastra_colaborador, name='cadastra_colaborador'),
    path('colaboradores/editar/<int:pk>/', views.edita_colaborador, name='edita_colaborador'),
    path('colaboradores/excluir/<int:pk>/', views.exclui_colaborador, name='exclui_colaborador'),

    # Equipamentos
    path('equipamentos/', views.lista_equipamentos, name='lista_equipamentos'),
    path('equipamentos/novo/', views.cadastra_equipamento, name='cadastra_equipamento'),
    path('equipamentos/editar/<int:pk>/', views.edita_equipamento, name='edita_equipamento'),
    path('equipamentos/excluir/<int:pk>/', views.exclui_equipamento, name='exclui_equipamento'),

    # Empréstimos
    path('emprestimos/', views.lista_emprestimos, name='lista_emprestimos'),
    path('emprestimos/novo/', views.cadastra_emprestimo, name='cadastra_emprestimo'),
    path('emprestimos/editar/<int:pk>/', views.edita_emprestimo, name='edita_emprestimo'),
    path('emprestimos/atualizar/<int:pk>/', views.atualiza_emprestimo, name='atualiza_emprestimo'),
    path('emprestimos/excluir/<int:pk>/', views.exclui_emprestimo, name='exclui_emprestimo'),
]