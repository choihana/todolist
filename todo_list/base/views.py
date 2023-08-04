from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Task
from django.urls import reverse_lazy


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'

class TaskCreate(CreateView):
    model = Task
    fields = ['user','title','description', 'complete']
    # 아이템 생성 성공 시, 리스트 화면으로 이동
    success_url = reverse_lazy('tasks')
