from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Tasks

class CreateTask(CreateView):
   model = Tasks
   fields = ['name', 'must_finish_by']
   template_name = 'todolist/tasks_form.html'
   success_url = reverse_lazy('list-task')

   def form_valid(self, form):
       form.instance.user = self.request.user
       return super(CreateTask,self).form_valid(form)

class DeleteTask(DeleteView):
    model = Tasks
    context_object_name = 'tasks'
    template_name = 'todolist/tasks_confirm_delete.html'
    success_url = reverse_lazy('list-task')

class UpdateTask(UpdateView):
    model = Tasks
    context_object_name = 'tasks'

class ListTask(ListView):
    model = Tasks
    context_object_name = 'tasks'
    template_name = 'todolist/tasks_list.html'






def say_hello(request):
    return HttpResponse("hello everybody. how are you? Lets go")

# Create your views here.
