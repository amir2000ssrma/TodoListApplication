from django.http import HttpResponse
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy

from .models import Tasks

class CreateTask(CreateView):
   model = Tasks
   fields = ['name', 'must_finish_by']
   template_name = 'todolist/tasks_form.html'
   success_url = reverse_lazy('list-task')

   def form_valid(self, form):
       form.instance.user = self.request.user
       return super().form_valid(form)

class ListTask(ListView):
    model = Tasks
    template_name = 'todolist/tasks_list.html'







def say_hello(request):
    return HttpResponse("hello everybody. how are you? Lets go")

# Create your views here.
