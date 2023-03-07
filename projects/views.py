from django.shortcuts import render
from projects.models import Project


# Create your views here.
def list_projects(request):
    projects_all = Project.objects.all()
    context = {"projects_all": projects_all}
    return render(request, "list.html", context)
