from django.urls import path
from .views import (home_view,
                    project_view,
                    )

app_name = 'ProjectReal'

urlpatterns = [
    path('', home_view, name='home-page'),
    path('project/<slug:slug>/', project_view, name='project-page'),
]
