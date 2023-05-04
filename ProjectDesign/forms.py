from django import forms
from .models import (Home,
                     About,
                     Intrest,
                     Project,
                     )


# Home Model
class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = '__all__'

    def get_class_name(self):
        return self.__class__.__name__


# About Model
class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

    def get_class_name(self):
        return self.__class__.__name__


# Intrest Model
class IntrestForm(forms.ModelForm):
    class Meta:
        model = Intrest
        fields = '__all__'

    def get_class_name(self):
        return self.__class__.__name__


# Project Model
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

    def get_class_name(self):
        return self.__class__.__name__
