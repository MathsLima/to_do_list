from django.shortcuts import render
from .models import Todo

#lista as tarefas cadastradas
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"todos": todos})

