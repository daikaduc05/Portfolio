from django.shortcuts import render
# Create your views here.
from .models import Project
def home(request):
    project = Project.objects.all()

    context = {
        'projects' : project
    }
    return render(request,'home.html',context)