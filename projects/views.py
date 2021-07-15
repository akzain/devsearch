from django.contrib.auth import login
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm

# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, "projects/projects.html", context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, "projects/single-project.html", {"project": projectObj, "owner": projectObj.owner})

@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            rd = form.save()
            return redirect("project", pk=rd.id)

    context = {"form": form}
    return render(request, "projects/project_form.html", context)

@login_required
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            rd = form.save()
            return redirect("project", pk=rd.id)

    context = {"form": form}
    return render(request, "projects/project_form.html", context)

@login_required
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects")
    context = {"object": project}
    return render(request, "projects/delete_template.html", context)

