from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        #login 성공 후 task-list 페이지로 이동
        return reverse_lazy('tasks')

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

class TaskUpdate(UpdateView):
    model = Task
    fields = ['user', 'title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')