from django.shortcuts import render, redirect
from projects.models import Project


# Create your views here.
def list_projects(request):
    if request.user.is_authenticated:
        projects_all = Project.objects.filter(owner=request.user)
        context = {"projects_all": projects_all}
        return render(request, "list.html", context)
    else:
        return redirect("login")
