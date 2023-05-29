from django.shortcuts import render, get_object_or_404, get_list_or_404
from ProjectDesign.models import (Home,
                                  About,
                                  Intrest,
                                  Project,
                                  )


def home_view(request):
    home = get_object_or_404(Home, title='Shubham Sahu')
    about = get_object_or_404(About, title='About Me')
    intrests = get_list_or_404(Intrest)
    projects = get_list_or_404(Project)

    template_name = 'ProjectModel/home-page.html'
    context = {
        'title': 'Home',
        'home': home,
        'about': about,
        'intrests': intrests,
        'projects': projects,
    }
    return render(request, template_name, context)


def project_view(request, slug):
    project = get_object_or_404(Project, slug=slug)

    template_name = 'ProjectModel/project-page.html'
    context = {
        'title': f'Project - {project.title}',
        'project': project,
    }
    return render(request, template_name, context)
