from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks_todo = Task.objects.filter(is_completed=False).order_by('-updated_at')
    tasks_completed = Task.objects.filter(is_completed=True).order_by('-updated_at')
    context = {
        'tasks_undone': tasks_todo,
        'tasks_done' : tasks_completed,
    }
    return render(request, 'home.html',context)