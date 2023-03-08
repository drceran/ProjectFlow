from django.shortcuts import render, redirect
from tasks.forms import CreateTaskForm
from tasks.models import Task

# Create your views here.


def create_task(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            saved_task = form.save()
            saved_task.save()
            return redirect("list_projects")
    else:
        form = CreateTaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)
