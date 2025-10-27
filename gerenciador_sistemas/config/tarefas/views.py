from django.shortcuts import get_object_or_404, redirect, render
from .models import Tarefa 
from django.http import HttpResponse

def listar_tarefas(request):
    tarefas_salvas = Tarefa.objects.all()
    contexto = {      
        'minhas_tarefas': tarefas_salvas
    }
    return render (request,  'tarefas/lista.html', contexto)

def detalhe_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)

    return render(request, 'tarefas/detalhe.html', {'tarefa': tarefa})

    def adicionar_Tarefa (request):
     if request.method == 'POST':
        Titulo = request.POST.Get('titulo')
        descricao = request.POST.Get('descricao')
        Tarefa.objects.create(titulo=titulo,descricao=descricao)

    return redirect('lista_tarefas')