from tabnanny import process_tokens
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Project

# Create your views here.

# Recommended
def homeView(request):
    # up_projects = 
    projects = Project.objects.all()
    context = {'projects': projects}

    return render(request, 'index.html', context)

# All projects
def projectsView(request):
    projects = Project.objects.all()
    context = {'projects': projects}

    return render(request, 'projects/projects.html', context)

def projectView(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    context = {'project': project,'tags': tags,}
    
    return render(request, 'projects/single-project.html', context)

# @login_required
# def like(request, pk):
#     if request.method == 'POST':
#          user = User.object.get(username=request.user.username)
#         project = Project.objects.get(id=pk)

#          new_like = Like(user=user, project=project)
#          new_like.already_liked = True

#         project.likes += 1
#         # project.user_likes.add(user)
#         project.save()
#         new_like.save()
#         return HttpResponseRedirect(reverse('index'))
            
