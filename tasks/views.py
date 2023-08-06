from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from . models import Task
from django.urls import reverse_lazy


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/index.html'


class CreatTaskView(CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'all_tasks']
    template_name = 'tasks/new_task.html'


class DetailTaskView(DetailView):
    model = Task


class UpdateTaskView(UpdateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'all_tasks']
    template_name_suffix = "_update_form"


class DeleteTaskView(DeleteView):
    model = Task
    success_url = 'task-list'
# def new_task(req):
#     tasks = Task.objects.all()
#     if req.method == ['POST']:
#         new = Task('aaa')
#         new.save()

