# todo/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import *
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required


# Create your views here.

class HomeView(View):
    template_name = 'todo/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

def testing(request):
    return render(request, 'todo/testing.html')
def calendar(request):
    return render(request, 'todo/calendar.html')
def board(request):
    return render(request, 'todo/board.html')
#def home(request):
#	return render(request, 'home.html')
	

'''
def index(request):
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/todo/list')


	context = {'tasks':tasks, 'form':form}
	return render(request, 'todo/list.html', context)
'''
def todo_list(request):
    # Your view logic
    return render(request, 'todo/list.html')

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
def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/todo/list')

	context = {'form':form}

	return render(request, 'todo/update_task.html', context)
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
    
def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/todo/list')

    context = {'item':item}
    return render(request, 'todo/delete.html', context)