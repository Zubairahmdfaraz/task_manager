from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_manager_app/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to the task list page
    else:
        form = TaskForm()

    return render(request, 'task_manager_app/add_task.html', {'form': form})

def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Redirect to the task list page
    else:
        form = TaskForm(instance=task)

    return render(request, 'task_manager_app/edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')  # Redirect to the task list page

    return render(request, 'task_manager_app/delete_task.html', {'task': task})
