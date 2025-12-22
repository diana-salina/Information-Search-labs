from django import forms
from .models import University, Student


class _DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs.setdefault("format", "%Y-%m-%d")
        super().__init__(**kwargs)


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = "__all__"
        labels = {
            "full_name": "Полное название",
            "short_name": "Сокращённое название",
            "foundation_date": "Дата создания",
        }
        widgets = {
            "foundation_date": _DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["foundation_date"].initial = self.instance.foundation_date


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        labels = {
            "full_name": "ФИО",
            "birth_date": "Дата рождения",
            "university": "Университет",
            "admission_year": "Год поступления",
        }
        widgets = {
            "birth_date": _DateInput(),
            "admission_year": forms.NumberInput(attrs={"min": 1900, "max": 2100}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields["birth_date"].initial = self.instance.birth_date
