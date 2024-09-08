from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    tag = request.POST['tag']
    Task.objects.create(task=task, tag=tag)
    return redirect('home')


def done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')


def editTask(request, pk):
    get_task = get_object_or_404(Task,pk=pk)
    
    if request.method == 'POST':
        updated_task = request.POST['task']
        updated_tag = request.POST['tag']
        get_task.task = updated_task
        get_task.tag = updated_tag
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
        return render(request, 'editTask.html', context)
    

def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')
