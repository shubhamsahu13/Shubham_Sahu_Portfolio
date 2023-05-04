from django.urls import path
from .views import (home_view,
                    project_view,
                    )

app_name = 'ProjectModel'

urlpatterns = [
    path('', home_view, name='home-page'),
    path('project/<slug>/', project_view, name='project-page'),
]
