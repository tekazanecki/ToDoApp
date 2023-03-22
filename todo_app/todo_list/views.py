from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = Task.objects.all
            messages.success(request, ("Item Has Been Added To List!"))
            return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = Task.objects.all
        return render(request, 'home.html', {'all_items': all_items})

def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    messages.success(request, ("Item Has Been Deleted"))
    return redirect('home')

def cross_off(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('home')

def uncross(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = False
    task.save()
    return redirect('home')

def edit(request, task_id):
    if request.method == 'POST':
        item = Task.objects.get(pk=task_id)

        form = TaskForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ("Item Has Been Edited!"))
            return redirect('home')
    else:
        item = Task.objects.get(pk=task_id)
        return render(request, 'edit.html', {'item': item})