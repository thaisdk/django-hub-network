from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def projectsView(request):
    return render(request, 'index.html')

def galleryView(request):
    return render(request, 'projects/projects.html')

def singleprojectView(request, pk):
    return render(request, 'projects/single-project.html')