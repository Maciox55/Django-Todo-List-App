from django.shortcuts import render, redirect
from app.models import Todo
from app.forms import TodoForm


def index(request):
    tasks = Todo.objects.all()
    context = {'tasks': tasks}

    return render(request, 'index.html', context)


def create_todo(request):
    form = TodoForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'index.html', context)


def complete_todo(request, id):
    task = Todo.objects.get(id=id)
    task.completed = True
    task.save()

    return redirect('index')


def delete_todo(request, id):
    task = Todo.objects.get(id=id)
    task.delete()
    return redirect('index')


def delete(request, id):
    task = Todo.objects.get(id=id)
    context = {'task': task}

    if request.method == 'POST':
        task = Todo.objects.get(id=id)
        task.delete()
        return redirect('index')

    return render(request, 'delete.html', context)


def update(request, id):
    task = Todo.objects.get(id=id)
    context = {'task': task}

    if request.method == 'POST':
        task = Todo.objects.get(id=id)
        form = TodoForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'update.html', context)

