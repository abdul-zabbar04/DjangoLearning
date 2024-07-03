from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import TaskModel
# Create your views here.
def add_task(request):
    if request.method== 'POST':
        task_form= TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('homePage')
    else:
        task_form= TaskForm()   
    return render(request, 'tasks/add_task.html', {'form': task_form})

def edit_task(request,id):
    target= TaskModel.objects.get(pk= id)
    task_form= TaskForm(instance=target)
    if request.method=='POST':
        task_form= TaskForm(request.POST, instance=target)
        if task_form.is_valid():
            task_form.save()
            return redirect('homePage')
    return render(request, 'tasks/add_task.html', {'form': task_form})


def delete_task(request, id):
    target= TaskModel.objects.get(pk= id).delete()
    return redirect('homePage')
