from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from ckeditor import fields


class Home(models.Model):
    title = models.CharField(max_length=20, unique=True, default='Apurv Chatur')
    subtitle = models.CharField(max_length=50, default='Django Web Developer')
    image = models.ImageField(upload_to='Home/', default='default.jpg')
    description = fields.RichTextField()
    slug = models.SlugField(unique=True, blank=True)

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    # ProjectDesign
    def get_object_list_url(self):
        return reverse('ProjectDesign:home-list-page')

    def get_object_create_url(self):
        return reverse('ProjectDesign:home-create-page')

    def get_object_retrieve_url(self):
        return reverse('ProjectDesign:home-retrieve-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_update_url(self):
        return reverse('ProjectDesign:home-update-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_delete_url(self):
        return reverse('ProjectDesign:home-delete-page',
                       kwargs={
                           'slug': self.slug
                       })


class About(models.Model):
    title = models.CharField(max_length=255, unique=True, default='About Me')
    subtitle = models.CharField(max_length=255, default='This section is about me!')
    image = models.ImageField(upload_to='About/', default='default.jpg')
    description = fields.RichTextField()
    resume = models.FileField(upload_to='About/', default='default.pdf')
    slug = models.SlugField(unique=True, blank=True)

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    # ProjectDesign
    def get_object_list_url(self):
        return reverse('ProjectDesign:about-list-page')

    def get_object_create_url(self):
        return reverse('ProjectDesign:about-create-page')

    def get_object_retrieve_url(self):
        return reverse('ProjectDesign:about-retrieve-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_update_url(self):
        return reverse('ProjectDesign:about-update-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_delete_url(self):
        return reverse('ProjectDesign:about-delete-page',
                       kwargs={
                           'slug': self.slug
                       })


class Intrest(models.Model):
    title = models.CharField(max_length=255, unique=True, default='Python')
    subtitle = models.CharField(max_length=255, default='I love it!')
    logo = models.CharField(max_length=255, default='Some logo')
    slug = models.SlugField(unique=True, blank=True)

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    # ProjectDesign
    def get_object_list_url(self):
        return reverse('ProjectDesign:intrest-list-page')

    def get_object_create_url(self):
        return reverse('ProjectDesign:intrest-create-page')

    def get_object_retrieve_url(self):
        return reverse('ProjectDesign:intrest-retrieve-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_update_url(self):
        return reverse('ProjectDesign:intrest-update-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_delete_url(self):
        return reverse('ProjectDesign:intrest-delete-page',
                       kwargs={
                           'slug': self.slug
                       })


class Project(models.Model):
    title = models.CharField(max_length=255, unique=True, default='Qrazzers')
    subtitle = models.CharField(max_length=255, default='Coding website!')
    image = models.ImageField(upload_to='Project/', default='default.jpg')
    description = fields.RichTextField()
    category = models.CharField(choices=
                                (('PP', 'Personal Project'),
                                 ('CP', 'Client Project')
                                 ),
                                max_length=2, blank=True, null=True)
    visit_url = models.URLField(max_length=255, default='https://github.com/ApurvChatur/')
    code_url = models.URLField(max_length=255, default='https://github.com/ApurvChatur/')
    slug = models.SlugField(unique=True, blank=True)

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

    # ProjectDesign
    def get_object_list_url(self):
        return reverse('ProjectDesign:project-list-page')

    def get_object_create_url(self):
        return reverse('ProjectDesign:project-create-page')

    def get_object_retrieve_url(self):
        return reverse('ProjectDesign:project-retrieve-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_update_url(self):
        return reverse('ProjectDesign:project-update-page',
                       kwargs={
                           'slug': self.slug
                       })

    def get_object_delete_url(self):
        return reverse('ProjectDesign:project-delete-page',
                       kwargs={
                           'slug': self.slug
                       })

    # Project Model
    def get_project_url(self):
        return reverse('ProjectModel:project-page',
                       kwargs={
                           'slug': self.slug
                       })

    # Project Real
    def get_real_project_url(self):
        return reverse('ProjectReal:project-page',
                       kwargs={
                           'slug': self.slug
                       })


class Certificate(models.Model):
    title = models.CharField(max_length=255, default='Certificate')
    subtitle = models.CharField(max_length=255, default='I love it!')
    file = models.FileField(upload_to='Certificate/', default='default.jpg')
    slug = models.SlugField(blank=True)

    # Some Common Methods
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    def get_class_name(self):
        return self.__class__.__name__

