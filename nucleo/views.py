from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Colaborador
from .forms import ColaboradorForm

def listar_colaboradores(request):
    query = request.GET.get('q', '')
    if query:
        colaboradores = Colaborador.objects.filter(nome__icontains=query)
    else:
        colaboradores = Colaborador.objects.all()
    return render(request, 'nucleo/index.html', {'colaboradores': colaboradores, 'query': query})

def criar_colaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador cadastrado com sucesso!')
            return redirect('criar_colaborador') # Fica na mesma tela conforme requisito
    else:
        form = ColaboradorForm()
    return render(request, 'nucleo/criar.html', {'form': form, 'titulo': 'Adicionar Colaborador'})

def editar_colaborador(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador atualizado com sucesso!')
            return redirect('listar_colaboradores')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'nucleo/criar.html', {'form': form, 'titulo': 'Editar Colaborador'})

def excluir_colaborador(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        colaborador.delete()
        messages.success(request, 'Colaborador excluído com sucesso!')
        return redirect('listar_colaboradores')
    return render(request, 'nucleo/excluir.html', {'colaborador': colaborador})