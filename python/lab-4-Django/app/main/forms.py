from django import forms
from .models import University, Student


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = "__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
