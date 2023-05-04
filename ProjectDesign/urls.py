from django.urls import path
from .views import (entry_view,

                    # Home Model
                    home_list_view,
                    home_create_view,
                    home_retrieve_view,
                    home_update_view,
                    home_delete_view,

                    # About Model
                    about_list_view,
                    about_create_view,
                    about_retrieve_view,
                    about_update_view,
                    about_delete_view,

                    # Intrest Model
                    intrest_list_view,
                    intrest_create_view,
                    intrest_retrieve_view,
                    intrest_update_view,
                    intrest_delete_view,

                    # Project Model
                    project_list_view,
                    project_create_view,
                    project_retrieve_view,
                    project_update_view,
                    project_delete_view,

                    )


app_name = 'ProjectDesign'

urlpatterns = [
    # Entry
    path('', entry_view, name='entry-page'),

    # Home Model
    path('home-list-page/', home_list_view, name='home-list-page'),
    path('home-create-page/', home_create_view, name='home-create-page'),
    path('home-retrieve-page/<slug>/', home_retrieve_view, name='home-retrieve-page'),
    path('home-update-page/<slug>/', home_update_view, name='home-update-page'),
    path('home-delete-page/<slug>/', home_delete_view, name='home-delete-page'),

    # About Model
    path('about-list-page/', about_list_view, name='about-list-page'),
    path('about-create-page/', about_create_view, name='about-create-page'),
    path('about-retrieve-page/<slug>/', about_retrieve_view, name='about-retrieve-page'),
    path('about-update-page/<slug>/', about_update_view, name='about-update-page'),
    path('about-delete-page/<slug>/', about_delete_view, name='about-delete-page'),

    # Intrest Model
    path('intrest-list-page/', intrest_list_view, name='intrest-list-page'),
    path('intrest-create-page/', intrest_create_view, name='intrest-create-page'),
    path('intrest-retrieve-page/<slug>/', intrest_retrieve_view, name='intrest-retrieve-page'),
    path('intrest-update-page/<slug>/', intrest_update_view, name='intrest-update-page'),
    path('intrest-delete-page/<slug>/', intrest_delete_view, name='intrest-delete-page'),

    # Project Model
    path('project-list-page/', project_list_view, name='project-list-page'),
    path('project-create-page/', project_create_view, name='project-create-page'),
    path('project-retrieve-page/<slug>/', project_retrieve_view, name='project-retrieve-page'),
    path('project-update-page/<slug>/', project_update_view, name='project-update-page'),
    path('project-delete-page/<slug>/', project_delete_view, name='project-delete-page'),
]
