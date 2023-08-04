from django.http import HttpResponse
from django.views.generic import CreateView,ListView,DeleteView
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
    success_url = reverse_lazy('list-task')

    def form_valid(self, form):
        return super(DeleteTask, self).form_valid()


class ListTask(ListView):
    model = Tasks
    context_object_name = 'tasks'
    template_name = 'todolist/tasks_list.html'



def ask_for_deleting(request, task_id):
    context = {'task_id': task_id}
    return render(request, 'todolist/task_deleting.html', context)



def say_hello(request):
    return HttpResponse("hello everybody. how are you? Lets go")

# Create your views here.
