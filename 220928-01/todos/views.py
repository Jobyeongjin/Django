from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
        
    }
    return render(request, 'todos/index.html', context)


def create(request):
    content = request.GET.get('content')
    deadline = request.GET.get('deadline')
    priority = request.GET.get('priority')
    Todo.objects.create(content=content, deadline=deadline, priority=priority)
    return redirect('todos:index')


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')


def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if todo.completed == False:
        todo.completed = True
    elif todo.completed == True:
        todo.completed = False
    todo.save()
    return redirect('todos:index')