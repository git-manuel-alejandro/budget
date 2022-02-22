from urllib import request
from django.shortcuts import render

# Create your views here.

def project_list(request):
    return render(request , 'budget/project-list.html')

def project_detail(request, project_slug):
    context = {
        'slug' : project_slug
    }
    return render(request , 'budget/project-detail.html'  , context)
