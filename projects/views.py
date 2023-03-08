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


# localhost:8000/projects/3
# buradaki 3, show project view indaki parametrelerde ikincisi olan id)
# user in  gormek istedigi projenin id si, parantez icinde olan.
def show_project(request, id):
    if not request.user.is_authenticated:
        return redirect("login")
    project_detail = Project.objects.get(id=id)
    context = {
        "project_detail": project_detail,
    }
    return render(request, "detail.html", context)


# def show_project(request, id):
#     if not request.user.is_authenticated:
#         return redirect("login")

#     project_categories = Project.objects.filter(
#         owner=request.user,
#         id=id,
#     )
#     context = {
#         "project_categories": project_categories,
#     }
#     return render(request, "detail.html", context)
# sol taraftaki seyler, projenin objelerinin attribute lari, sag taraftaki seyler browser dan gelen request e iliskin seyler.

# def show_project(request, id):
#     project= get_object_or_404(Project, pk=id)
#     return render(request, )


# def task_properties(request):
#     if not request.user.is_authenticated:
#         return redirect("login")
#     task_categories = Task.objects.all()
#     context = {
#         "task_categories":task
#     }
