from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, 'todos/index.html', {
        'todos': todos,
    })


def create(request):
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')
    Todo.objects.create(content=content, priority=priority, deadline=deadline)
    return redirect('todos:index')


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todos:index')


def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.completed == False:
        todo.completed = True
    elif todo.completed == True:
        todo.completed = False
    todo.save()
    return redirect('todos:index')


def edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    return render(request, 'todos/edit.html', {
        'todo': todo,
    })


def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    return render(request, 'todos/detail.html', {
        'todo': todo,
    })


def rewrite(request, pk):
    todo = Todo.objects.get(pk=pk)
    content = request.GET.get('content')
    todo.content = content
    todo.save()
    return redirect('todos:detail', todo.pk)