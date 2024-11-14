from django.shortcuts import render
from projects.models import Project, Technology


# Create your views here.

def project_index(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render (request, "projects/project_index.html", context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render (request, "projects/project_detail.html", context)


def technology(request):
    technologies = Technology.objects.all()
    context = {'technologies': technologies}
    return render (request,"projects/project_index.html", context)