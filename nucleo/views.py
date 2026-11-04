from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Colaborador, Equipamento, EmprestimoEPI
from .forms import ColaboradorForm, EquipamentoForm, EmprestimoEPIForm

@login_required
def dashboard(request):
    total_colaboradores = Colaborador.objects.count()
    total_equipamentos = Equipamento.objects.count()
    total_emprestimos = EmprestimoEPI.objects.count()
    emprestimos_ativos = EmprestimoEPI.objects.filter(status='Emprestado').count()
    
    context = {
        'total_colaboradores': total_colaboradores,
        'total_equipamentos': total_equipamentos,
        'total_emprestimos': total_emprestimos,
        'emprestimos_ativos': emprestimos_ativos,
    }
    return render(request, 'nucleo/index.html', context)

# --- COLABORADORES ---
@login_required
def lista_colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'nucleo/lista_colaboradores.html', {'colaboradores': colaboradores})

@login_required
def cadastra_colaborador(request):
    if not request.user.is_superuser and not request.user.has_perm('nucleo.add_colaborador'):
        messages.error(request, 'Acesso negado: Não tens permissão para cadastrar colaboradores.')
        return redirect('nucleo:lista_colaboradores')
        
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador cadastrado com sucesso!')
            return redirect('nucleo:lista_colaboradores')
    else:
        form = ColaboradorForm()
    return render(request, 'nucleo/criar.html', {'form': form, 'titulo': 'Registrar Colaborador'})

@login_required
def edita_colaborador(request, pk):
    if not request.user.is_superuser and not request.user.has_perm('nucleo.change_colaborador'):
        messages.error(request, 'Acesso negado: Não tens permissão para editar colaboradores.')
        return redirect('nucleo:lista_colaboradores')
        
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador atualizado com sucesso!')
            return redirect('nucleo:lista_colaboradores')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'nucleo/criar.html', {'form': form, 'titulo': 'Editar Colaborador'})

@login_required
def exclui_colaborador(request, pk):
    if not request.user.is_superuser and not request.user.has_perm('nucleo.delete_colaborador'):
        messages.error(request, 'Acesso negado: Não tens permissão para excluir colaboradores.')
        return redirect('nucleo:lista_colaboradores')
        
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        colaborador.delete()
        messages.success(request, 'Colaborador excluído com sucesso!')
        return redirect('nucleo:lista_colaboradores')
    return render(request, 'excluir.html', {'objeto': colaborador})

# --- EQUIPAMENTOS ---
@login_required
def lista_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'nucleo/lista_equipamentos.html', {'equipamentos': equipamentos})

@login_required
def cadastra_equipamento(request):
    if not request.user.is_superuser and not request.user.has_perm('nucleo.add_equipamento'):
        messages.error(request, 'Acesso negado: Não tens permissão para cadastrar equipamentos.')
        return redirect('nucleo:lista_equipamentos')
        
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento cadastrado com sucesso!')
            return redirect('nucleo:lista_equipamentos')
    else:
        form = EquipamentoForm()
    return render(request, 'nucleo/criar.html', {'form': form, 'titulo': 'Registrar Equipamento'})

@login_required
def edita_equipamento(request, pk):
    if not request.user.is_superuser and not request.user.has_perm('nucleo.change_equipamento'):
        messages.error(request, 'Acesso negado: Não tens permissão para editar equipamentos.')
        return redirect('nucleo:lista_equipamentos')
        
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento atualizado com sucesso!')
            return redirect('nucleo:lista_equipamentos')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'nucleo/criar.html', {'form': form, 'titulo': 'Editar Equipamento'})

@login_required
def exclui_equipamento(request, pk):
    if not request.user.is_superuser and not request.user.has_perm('nucleo.delete_equipamento'):
        messages.error(request, 'Acesso negado: Não tens permissão para excluir equipamentos.')
        return redirect('nucleo:lista_equipamentos')
        
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.delete()
        messages.success(request, 'Equipamento excluído com sucesso!')
        return redirect('nucleo:lista_equipamentos')
    return render(request, 'excluir.html', {'objeto': equipamento})

# --- EMPRÉSTIMOS ---
@login_required
def lista_emprestimos(request):
    emprestimos = EmprestimoEPI.objects.all()
    
    colaborador_nome = request.GET.get('colaborador')
    equipamento_nome = request.GET.get('equipamento')
    status_filtro = request.GET.get('status')
    
    if colaborador_nome:
        emprestimos = emprestimos.filter(colaborador__nome__icontains=colaborador_nome)
    if equipamento_nome:
        emprestimos = emprestimos.filter(equipamento__nome__icontains=equipamento_nome)
    if status_filtro and status_filtro != 'Todos':
        emprestimos = emprestimos.filter(status=status_filtro)
        
    status_choices = EmprestimoEPI._meta.get_field('status').choices
    
    context = {
        'emprestimos': emprestimos,
        'colaborador_nome': colaborador_nome,
        'equipamento_nome': equipamento_nome,
        'status_filtro': status_filtro,
        'status_choices': status_choices,
    }
    return render(request, 'nucleo/lista_emprestimos.html', context)

@login_required
def cadastra_emprestimo(request):
    # O usuário comum TEM permissão para registrar empréstimos.
    if request.method == 'POST':
        form = EmprestimoEPIForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            equipamento = emprestimo.equipamento
            
            # Se o status inicial retira do estoque (Emprestado, Fornecido, Perdido ou Danificado)
            if emprestimo.status in ['Emprestado', 'Fornecido', 'Perdido', 'Danificado']:
                if equipamento.quantidade_estoque >= emprestimo.quantidade:
                    equipamento.quantidade_estoque -= emprestimo.quantidade
                    equipamento.save()
                else:
                    form.add_error('quantidade', 'Quantidade indisponível em estoque!')
                    return render(request, 'nucleo/criar.html', {'form': form, 'titulo': 'Registrar Empréstimo de EPI', 'is_emprestimo': True})
            
            emprestimo.save()
            messages.success(request, 'Empréstimo registrado com sucesso!')
            return redirect('nucleo:lista_emprestimos')
    else:
        form = EmprestimoEPIForm()
    return render(request, 'nucleo/criar.html', {'form': form, 'titulo': 'Registrar Empréstimo de EPI', 'is_emprestimo': True})


@login_required
def edita_emprestimo(request, pk):
    # Permite se for superuser OU se tiver a permissão específica dada no Admin
    if not request.user.is_superuser and not request.user.has_perm('nucleo.change_emprestimoepi'):
        messages.error(request, 'Acesso negado: Não tens permissão para editar empréstimos.')
        return redirect('nucleo:lista_emprestimos')

    emprestimo_antigo = get_object_or_404(EmprestimoEPI, pk=pk)
    status_antigo = emprestimo_antigo.status
    quantidade_antiga = emprestimo_antigo.quantidade
    equipamento_antigo = emprestimo_antigo.equipamento

    if request.method == 'POST':
        form = EmprestimoEPIForm(request.POST, instance=emprestimo_antigo)
        if form.is_valid():
            emprestimo_novo = form.save(commit=False)
            equipamento_novo = emprestimo_novo.equipamento
            
            # Verificar se o estado anterior mantinha o estoque baixado
            estava_fora = status_antigo in ['Emprestado', 'Fornecido', 'Perdido', 'Danificado']
            vai_ficar_fora = emprestimo_novo.status in ['Emprestado', 'Fornecido', 'Perdido', 'Danificado']
            
            # Transição 1: Estava fora e passou a Devolvido -> DEVOLVE ao estoque
            if estava_fora and not vai_ficar_fora:
                equipamento_antigo.quantidade_estoque += quantidade_antiga
                equipamento_antigo.save()
                
            # Transição 2: Estava Devolvido e passou para um estado que retira/mantém fora -> DEBITA do estoque
            elif not estava_fora and vai_ficar_fora:
                if equipamento_novo.quantidade_estoque >= emprestimo_novo.quantidade:
                    equipamento_novo.quantidade_estoque -= emprestimo_novo.quantidade
                    equipamento_novo.save()
                else:
                    form.add_error('quantidade', 'Quantidade indisponível em estoque!')
                    # Mantém as datas preenchidas se der erro
                    if emprestimo_antigo.data_emprestimo:
                        form.initial['data_emprestimo'] = emprestimo_antigo.data_emprestimo.strftime('%Y-%m-%d')
                    if emprestimo_antigo.data_prevista_devolucao:
                        form.initial['data_prevista_devolucao'] = emprestimo_antigo.data_prevista_devolucao.strftime('%Y-%m-%d')
                    return render(request, 'nucleo/criar.html', {'form': form, 'titulo': 'Editar Empréstimo de EPI', 'is_emprestimo': True})
            
            emprestimo_novo.save()
            messages.success(request, 'Empréstimo atualizado com sucesso!')
            return redirect('nucleo:lista_emprestimos')
    else:
        form = EmprestimoEPIForm(instance=emprestimo_antigo)
        
        # Mantém as datas visíveis no formulário de edição
        if emprestimo_antigo.data_emprestimo:
            form.initial['data_emprestimo'] = emprestimo_antigo.data_emprestimo.strftime('%Y-%m-%d')
        if emprestimo_antigo.data_prevista_devolucao:
            form.initial['data_prevista_devolucao'] = emprestimo_antigo.data_prevista_devolucao.strftime('%Y-%m-%d')

    return render(request, 'nucleo/criar.html', {'form': form, 'titulo': 'Editar Empréstimo de EPI', 'is_emprestimo': True})


@login_required
def atualiza_emprestimo(request, pk):
    if not request.user.is_superuser and not request.user.has_perm('nucleo.change_emprestimoepi'):
        messages.error(request, 'Acesso negado: Não tens permissão para alternar status.')
        return redirect('nucleo:lista_emprestimos')
    
    emprestimo = get_object_or_404(EmprestimoEPI, pk=pk)
    equipamento = emprestimo.equipamento
    
    if emprestimo.status in ['Emprestado', 'Fornecido', 'Perdido', 'Danificado']:
        emprestimo.status = 'Devolvido'
        equipamento.quantidade_estoque += emprestimo.quantidade
        equipamento.save()
        messages.success(request, 'Status alterado para Devolvido! Estoque reposto.')
        
    elif emprestimo.status == 'Devolvido':
        if equipamento.quantidade_estoque >= emprestimo.quantidade:
            emprestimo.status = 'Emprestado'
            equipamento.quantidade_estoque -= emprestimo.quantidade
            equipamento.save()
            messages.success(request, 'Status alterado para Emprestado! Estoque debitado.')
        else:
            messages.error(request, 'Erro: Quantidade insuficiente em estoque para reativar o empréstimo!')
            return redirect('nucleo:lista_emprestimos')
            
    emprestimo.save()
    return redirect('nucleo:lista_emprestimos')


@login_required
def exclui_emprestimo(request, pk):
    # Permite se for superuser OU se tiver a permissão de excluir empréstimos que marcaste no Admin
    if not request.user.is_superuser and not request.user.has_perm('nucleo.delete_emprestimoepi'):
        messages.error(request, 'Acesso negado: Não tens permissão para excluir empréstimos.')
        return redirect('nucleo:lista_emprestimos')
        
    emprestimo = get_object_or_404(EmprestimoEPI, pk=pk)
    if request.method == 'POST':
        if emprestimo.status in ['Emprestado', 'Fornecido', 'Perdido', 'Danificado']:
            equipamento = emprestimo.equipamento
            equipamento.quantidade_estoque += emprestimo.quantidade
            equipamento.save()
            
        emprestimo.delete()
        messages.success(request, 'Empréstimo excluído com sucesso e estoque regularizado!')
        return redirect('nucleo:lista_emprestimos')
        
    return render(request, 'excluir.html', {'objeto': emprestimo})