from django.urls import path
from . import views
from .views import CreateTask, ListTask

urlpatterns = [
    path("", views.say_hello, name = "say_hello"),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('list-task/', ListTask.as_view(), name='list-task'),
]