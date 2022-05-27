from http.client import HTTPResponse
# from msilib.schema import File
from multiprocessing import context
from turtle import back
from winreg import REG_QWORD
from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.conf import settings
from . import forms 
from .models import Project, Frontend, Backend
import os
import shutil

fInput = ""
bInput = ""

def index(request):
    form = forms.FrontendForm()
    context = {
        'form': form,
    }
    return render(request, 'AppGenerator/index1.html', context)

def backendForm(request):
    global fInput
    if request.method=="POST":
        form = forms.FrontendForm(request.POST)
        if form.is_valid():
            fName = form.cleaned_data['frontend']
            fInput = fName
            fObj = Frontend.objects.get(fName=fInput)
            bList = fObj.backends.all()
    context = {
        'choices': bList
    }
    return render(request, 'AppGenerator/index2.html', context)

def searchProjectFolder(request):
    if request.method=="POST":
        if request.POST.get("backend") not in ["",None]:
            global bInput, fInput
            bInput = request.POST.get("backend")
            
            fInput = "_dot_".join(fInput.split("."))
            bInput = "_dot_".join(bInput.split("."))
            # print(fInput, bInput)
            return HttpResponseRedirect("/setup/"+fInput+"-"+bInput) 
    else:
        return HttpResponseRedirect("/backend-form")      

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read(), content_type='attachment/zip')
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404


def setup(request, frontend, backend):
    docFileName = frontend + "-" + backend + ".txt"
    documentation = []
    with open(os.path.join(os.path.abspath("./static/docs/"),docFileName), "r") as f:
        for line in f.readlines():
            line = "".join(line.split("\t"))
            line = "".join(line.split("\n"))
            documentation .append(line)
    f.close()
    
    frontend = ".".join(frontend.split("_dot_"))
    backend = ".".join(backend.split("_dot_"))
    print(frontend, backend)
    project = Project.objects.get(frontend=frontend, backend=backend)
    context = {
        'project': project,
        'documentation': documentation
    }
    return render(request, 'AppGenerator/setup.html', context)