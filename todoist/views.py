from django.shortcuts import get_object_or_404, redirect, render

from .forms import TodoForm
from .models import Todo


# Create your views here.
def index(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TodoForm()
        todos = Todo.objects.all()
        context = {"todos": todos, "form": form}

    return render(request, "todoist/index.html", context)


def create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TodoForm()

    return render(request, "todoist/create.html", {"form": form})


def delete(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    todo.delete()
    return redirect("home")


def toggle_todo_status(request, todo_pk):
    """
    Toggle todo status Done <-> Not Done
    """
    todo = get_object_or_404(Todo, pk=todo_pk)
    if todo.status == Todo.Status.DONE:
        todo.status = Todo.Status.NOT_DONE
    elif todo.status == Todo.Status.NOT_DONE:
        todo.status = Todo.Status.DONE
    todo.save()

    return redirect("home")
