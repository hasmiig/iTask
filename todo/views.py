# todo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import *
from .forms import *
from .models import Task
from .forms import TaskForm, TaskUpdateForm, LabelForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.urls import reverse
# Create your views here.

class HomeView(View):
    template_name = 'todo/home.html'

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(user=request.user)
        return render(request, self.template_name, {'tasks': tasks})

def testing(request):
    return render(request, 'todo/testing.html')
def calendar(request):
    return render(request, 'todo/calendar.html')
def board(request):
    return render(request, 'todo/board.html')
#def home(request):
#	return render(request, 'home.html')
	

def todo_list(request):
    # Your original view logic without tasks
    return render(request, 'todo/list.html')

@login_required
def todo_list_with_tasks(request):
    user=request.user
    tasks = Task.objects.filter(user)
    return render(request, 'todo/home.html', {'tasks': tasks})

'''
@login_required
def index(request):
    user = request.user

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()
            return redirect('todo_list')  # Corrected the redirect URL
    else:
        form = TaskForm()

    tasks = Task.objects.filter(user=user)
    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/list.html', context)
'''

'''
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    # Check if the current user owns the task
    if request.user != task.user:
        # Handle unauthorized access, for example, redirect to a 403 page
        return render(request, '403.html', status=403)

    form = TaskForm(request.POST or None, instance=task)

    if request.method == 'POST':
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Set the user before saving
            task.save()
            return redirect('todo_list')

    context = {'form': form}
    return render(request, 'todo/update_task.html', context)
    
'''

from django.shortcuts import render, redirect
from django.http import JsonResponse

def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        update_form = TaskUpdateForm(request.POST, instance=task)
        if update_form.is_valid():
            # Update the task with the form data
            update_form.save()

            # Redirect to the task list
            return redirect('todo_list')

    else:
        # Create the form with initial data from the task
        update_form = TaskUpdateForm(instance=task)

    return render(request, 'todo/update_task.html', {'update_form': update_form, 'task': task})

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/todo/list')

    context = {'item':item}
    return render(request, 'todo/delete.html', context)


def create_task(request):
    user = request.user
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Process the form data, including the selected deadline
            title = form.cleaned_data['title']
            deadline = form.cleaned_data['deadline']
            description = form.cleaned_data['description']

            # Check if the deadline is before today
            if deadline and deadline < timezone.now().date():
                form.add_error('deadline', 'Deadline cannot be set before today.')
                return render(request, 'todo/list.html', {'form': form})

            # Save the task to the database
            task = Task(user=user, title=title, deadline=deadline, description=description)
            task.save()

            # Redirect to a success page or the task list
            return redirect('todo_list')  # Update with your URL name

    else:
        form = TaskForm()

    tasks = Task.objects.filter(user=user)
    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/list.html', context)


def label_popup(request):
    if request.method == 'POST':
        form = LabelForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = {field: form.errors[field][0] for field in form.errors}
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = LabelForm()

    return render(request, 'todo/label_popup.html', {'form': form})
