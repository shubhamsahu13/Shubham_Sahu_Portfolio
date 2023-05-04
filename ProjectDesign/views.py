from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import (Home,
                     About,
                     Intrest,
                     Project,
                     )
from .forms import (HomeForm,
                    AboutForm,
                    IntrestForm,
                    ProjectForm,
                    )


def entry_view(request):
    template_name = 'ProjectDesign/entry-page.html'
    context = {
        'title': 'Entry Page'
    }
    return render(request, template_name, context)


# Home Model (LCRUD)
# Home List
@staff_member_required()
def home_list_view(request):
    objects_list = Home.objects.all()

    template_name = 'ProjectDesign/Home/a-home-list-page.html'
    context = {
        'title': 'Home List',
        'objects_list': objects_list
    }
    return render(request, template_name, context)

# Home Create
@staff_member_required()
def home_create_view(request):
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:home-list-page')
    else:
        form = HomeForm()

    template_name = 'ProjectDesign/Home/b-home-create-page.html'
    context = {
        'title': 'Home Create',
        'object_form': form,
    }
    return render(request, template_name, context)

# Home Retrieve
@staff_member_required()
def home_retrieve_view(request, slug):
    object = get_object_or_404(Home, slug=slug)

    template_name = 'ProjectDesign/Home/c-home-retrieve-page.html'
    context = {
        'title': 'Home Retrieve',
        'object': object,
    }
    return render(request, template_name, context)

# Home Update
@staff_member_required()
def home_update_view(request, slug):
    object = get_object_or_404(Home, slug=slug)

    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:home-list-page')
    else:
        form = HomeForm(instance=object)

    template_name = 'ProjectDesign/Home/d-home-update-page.html'
    context = {
        'title': 'Home Update',
        'object_form': form,
    }
    return render(request, template_name, context)

# Home Delete
@staff_member_required()
def home_delete_view(request, slug):
    if request.method == 'POST':
        object = get_object_or_404(Home, slug=slug)
        object.delete()
        return redirect('ProjectDesign:home-list-page')
    else:
        object = get_object_or_404(Home, slug=slug)

    template_name = 'ProjectDesign/Home/e-home-delete-page.html'
    context = {
        'title': 'Home Delete',
        'object': object,
    }
    return render(request, template_name, context)


# About Model (LCRUD)
# About List
@staff_member_required()
def about_list_view(request):
    objects_list = About.objects.all()

    template_name = 'ProjectDesign/About/a-about-list-page.html'
    context = {
        'title': 'About List',
        'objects_list': objects_list
    }
    return render(request, template_name, context)

# About Create
@staff_member_required()
def about_create_view(request):
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:about-list-page')
    else:
        form = AboutForm()

    template_name = 'ProjectDesign/About/b-about-create-page.html'
    context = {
        'title': 'About Create',
        'object_form': form,
    }
    return render(request, template_name, context)

# About Retrieve
@staff_member_required()
def about_retrieve_view(request, slug):
    object = get_object_or_404(About, slug=slug)

    template_name = 'ProjectDesign/About/c-about-retrieve-page.html'
    context = {
        'title': 'About Retrieve',
        'object': object,
    }
    return render(request, template_name, context)

# About Update
@staff_member_required()
def about_update_view(request, slug):
    object = get_object_or_404(About, slug=slug)

    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:about-list-page')
    else:
        form = AboutForm(instance=object)

    template_name = 'ProjectDesign/About/d-about-update-page.html'
    context = {
        'title': 'About Update',
        'object_form': form,
    }
    return render(request, template_name, context)

# About Delete
@staff_member_required()
def about_delete_view(request, slug):
    if request.method == 'POST':
        object = get_object_or_404(About, slug=slug)
        object.delete()
        return redirect('ProjectDesign:about-list-page')
    else:
        object = get_object_or_404(About, slug=slug)

    template_name = 'ProjectDesign/About/e-about-delete-page.html'
    context = {
        'title': 'About Delete',
        'object': object,
    }
    return render(request, template_name, context)


# Intrest Model (LCRUD)
# Intrest List
@staff_member_required()
def intrest_list_view(request):
    objects_list = Intrest.objects.all()

    template_name = 'ProjectDesign/Intrest/a-intrest-list-page.html'
    context = {
        'title': 'Intrest List',
        'objects_list': objects_list
    }
    return render(request, template_name, context)

# Intrest Create
@staff_member_required()
def intrest_create_view(request):
    if request.method == 'POST':
        form = IntrestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:intrest-list-page')
    else:
        form = IntrestForm()

    template_name = 'ProjectDesign/Intrest/b-intrest-create-page.html'
    context = {
        'title': 'Intrest Create',
        'object_form': form,
    }
    return render(request, template_name, context)

# Intrest Retrieve
@staff_member_required()
def intrest_retrieve_view(request, slug):
    object = get_object_or_404(Intrest, slug=slug)

    template_name = 'ProjectDesign/Intrest/c-intrest-retrieve-page.html'
    context = {
        'title': 'Intrest Retrieve',
        'object': object,
    }
    return render(request, template_name, context)

# Intrest Update
@staff_member_required()
def intrest_update_view(request, slug):
    object = get_object_or_404(Intrest, slug=slug)

    if request.method == 'POST':
        form = IntrestForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:intrest-list-page')
    else:
        form = IntrestForm(instance=object)

    template_name = 'ProjectDesign/Intrest/d-intrest-update-page.html'
    context = {
        'title': 'Intrest Update',
        'object_form': form,
    }
    return render(request, template_name, context)

# Intrest Delete
@staff_member_required()
def intrest_delete_view(request, slug):
    if request.method == 'POST':
        object = get_object_or_404(Intrest, slug=slug)
        object.delete()
        return redirect('ProjectDesign:intrest-list-page')
    else:
        object = get_object_or_404(Intrest, slug=slug)

    template_name = 'ProjectDesign/Intrest/e-intrest-delete-page.html'
    context = {
        'title': 'Intrest Delete',
        'object': object,
    }
    return render(request, template_name, context)


# Project Model (LCRUD)
# Project List
@staff_member_required()
def project_list_view(request):
    objects_list = Project.objects.all()

    template_name = 'ProjectDesign/Project/a-project-list-page.html'
    context = {
        'title': 'Project List',
        'objects_list': objects_list
    }
    return render(request, template_name, context)

# Project Create
@staff_member_required()
def project_create_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:project-list-page')
    else:
        form = ProjectForm()

    template_name = 'ProjectDesign/Project/b-project-create-page.html'
    context = {
        'title': 'Project Create',
        'object_form': form,
    }
    return render(request, template_name, context)

# Project Retrieve
@staff_member_required()
def project_retrieve_view(request, slug):
    object = get_object_or_404(Project, slug=slug)

    template_name = 'ProjectDesign/Project/c-project-retrieve-page.html'
    context = {
        'title': 'Project Retrieve',
        'object': object,
    }
    return render(request, template_name, context)

# Project Update
@staff_member_required()
def project_update_view(request, slug):
    object = get_object_or_404(Project, slug=slug)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect('ProjectDesign:project-list-page')
    else:
        form = ProjectForm(instance=object)

    template_name = 'ProjectDesign/Project/d-project-update-page.html'
    context = {
        'title': 'Project Update',
        'object_form': form,
    }
    return render(request, template_name, context)

# Project Delete
@staff_member_required()
def project_delete_view(request, slug):
    if request.method == 'POST':
        object = get_object_or_404(Project, slug=slug)
        object.delete()
        return redirect('ProjectDesign:project-list-page')
    else:
        object = get_object_or_404(Project, slug=slug)

    template_name = 'ProjectDesign/Project/e-project-delete-page.html'
    context = {
        'title': 'Project Delete',
        'object': object,
    }
    return render(request, template_name, context)
