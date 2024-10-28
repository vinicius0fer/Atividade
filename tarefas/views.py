from django.shortcuts import render

def lista_tarefas(request):
    tarefas = ("Estudar Django", "Criar um projeto", "Revisar o material")
    return render(request, 'tarefas/lista.html', {'tarefas': tarefas})
