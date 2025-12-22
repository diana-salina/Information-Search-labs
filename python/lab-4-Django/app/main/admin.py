from django.contrib import admin
from .models import University, Student


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ("full_name", "short_name", "foundation_date")
    search_fields = ("full_name", "short_name")
    list_filter = ("foundation_date",)
    ordering = ("full_name",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "birth_date", "university", "admission_year")
    list_filter = ("university", "admission_year")
    search_fields = ("full_name",)
    ordering = ("full_name",)
    raw_id_fields = ("university",)
