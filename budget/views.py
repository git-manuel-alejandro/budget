from django.shortcuts import get_object_or_404, render
from .import models
from django.views.generic import CreateView
# Create your views here.

def project_list(request):
    return render(request , 'budget/project-list.html')

def project_detail(request, project_slug):
    # project = models.Project.objects.get(slug = project_slug)
    project = get_object_or_404(models.Project , slug = project_slug)
    expenses_list = project.expenses.all()
    context = {
        'project' : project,
        'expenses_list' : expenses_list
    }
    return render(request , 'budget/project-detail.html'  , context)


class ProjectCreateView(CreateView):
    model = models.Project
    template_name = 'budget/add-project.html'
    fields = ('name' , 'budget')