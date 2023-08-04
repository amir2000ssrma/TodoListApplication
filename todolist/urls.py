from django.urls import path
from . import views
from .views import CreateTask, ListTask, DeleteTask

urlpatterns = [
    path("", views.say_hello, name = "say_hello"),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('list-task/', ListTask.as_view(), name='list-task'),
    path('delete-task/', DeleteTask.as_view(), name='delete-task'),
    path('<int:task_id>/deleting/', views.ask_for_deleting, name='deleting'),
]