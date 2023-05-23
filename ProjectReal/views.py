from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.mail import send_mail
from ProjectDesign.models import (Home,
                                  About,
                                  Intrest,
                                  Project,
                                  Certificate
                                  )


def home_view(request):
    home = get_object_or_404(Home, title='Shubham Sahu')
    about = get_object_or_404(About, title='About Me')
    interests = get_list_or_404(Intrest)
    projects = get_list_or_404(Project)
    certificates = get_list_or_404(Certificate)

    if request.method == "POST":
        send_mail(
            subject='Thanks',
            message='Thanks for visit',
            from_email='shubhamsahu1315@gmail.com',
            recipient_list=['shubhamsahu1315@gmail.com']
        )

    template_name = 'ProjectReal/home-page.html'
    context = {
        'home': home,
        'about': about,
        'interests': interests,
        'projects': projects,
        'certificates': certificates,
    }
    return render(request, template_name, context)


def project_view(request, slug):
    project = get_object_or_404(Project, slug=slug)

    template_name = 'ProjectReal/project-page.html'
    context = {
        'project': project,
    }
    return render(request, template_name, context)

