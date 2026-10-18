from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Colaborador, Equipamento, EmprestimoEPI
from .forms import ColaboradorForm, EquipamentoForm, EmprestimoEPIForm

def index(request):
    query = request.GET.get('busca', '')
    if query:
        colaboradores = Colaborador.objects.filter(nome__icontains=query)
    else:
        colaboradores = Colaborador.objects.all()

    context = {
        'total_colaboradores': Colaborador.objects.count(),
        'total_equipamentos': Equipamento.objects.count(),
        'total_emprestimos': EmprestimoEPI.objects.filter(status='Emprestado').count(),
        'colaboradores': colaboradores,  # <-- Adiciona esta linha
        'busca': query,                  # <-- E esta linha
    }
    return render(request, 'nucleo/index.html', context)

# --- COLABORADORES ---
def lista_colaboradores(request):
    query = request.GET.get('busca', '')
    if query:
        colaboradores = Colaborador.objects.filter(nome__icontains=query)
    else:
        colaboradores = Colaborador.objects.all()
    return render(request, 'nucleo/lista_colaboradores.html', {'colaboradores': colaboradores, 'busca': query})

def cadastra_colaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador cadastrado com sucesso!')
            return redirect('lista_colaboradores')
        else:
            messages.error(request, 'Erro ao cadastrar colaborador. Verifique os dados.')
    else:
        form = ColaboradorForm()
    
    # Altere esta linha para apontar para o seu 'criar.html':
    return render(request, 'nucleo/criar.html', {'form': form})

def edita_colaborador(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador atualizado com sucesso!')
            return redirect('lista_colaboradores')
        else:
            messages.error(request, 'Erro ao atualizar colaborador.')
    else:
        form = ColaboradorForm(instance=colaborador)
    
    # Altere esta linha para apontar para o 'criar.html':
    return render(request, 'nucleo/criar.html', {'form': form})

def exclui_colaborador(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    colaborador.delete()
    messages.success(request, 'Colaborador excluído com sucesso!')
    return redirect('lista_colaboradores')


# --- EQUIPAMENTOS ---
def lista_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'nucleo/lista_equipamentos.html', {'equipamentos': equipamentos})

def cadastra_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento cadastrado com sucesso!')
            return redirect('lista_equipamentos')
        else:
            messages.error(request, 'Erro ao cadastrar equipamento.')
    else:
        form = EquipamentoForm()
    return render(request, 'nucleo/criar.html', {'form': form})

def edita_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipamento atualizado com sucesso!')
            return redirect('lista_equipamentos')
        else:
            messages.error(request, 'Erro ao atualizar equipamento.')
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'nucleo/criar.html', {'form': form})

def exclui_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    equipamento.delete()
    messages.success(request, 'Equipamento excluído com sucesso!')
    return redirect('lista_equipamentos')


# --- EMPRÉSTIMOS DE EPI ---
def lista_emprestimos(request):
    emprestimos = EmprestimoEPI.objects.all()
    return render(request, 'nucleo/lista_emprestimos.html', {'emprestimos': emprestimos})

def cadastra_emprestimo(request):
    if request.method == 'POST':
        form = EmprestimoEPIForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empréstimo registrado com sucesso!')
            return redirect('lista_emprestimos')
        else:
            messages.error(request, 'Erro ao registrar empréstimo.')
    else:
        form = EmprestimoEPIForm()
    return render(request, 'nucleo/criar.html', {'form': form})