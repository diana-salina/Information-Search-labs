from django.shortcuts import render, get_object_or_404, redirect
from .models import University, Student
from .forms import UniversityForm, StudentForm

def university_list(request):
    universities = University.objects.all()
    return render(request, "main/university_list.html", {"universities": universities})


def university_create(request):
    if request.method == "POST":
        form = UniversityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("university_list")
    else:
        form = UniversityForm()
    return render(request, "main/university_form.html", {"form": form})


def university_update(request, pk):
    university = get_object_or_404(University, pk=pk)
    if request.method == "POST":
        form = UniversityForm(request.POST, instance=university)
        if form.is_valid():
            form.save()
            return redirect("university_list")
    else:
        form = UniversityForm(instance=university)
    return render(request, "main/university_form.html", {"form": form})


def university_delete(request, pk):
    university = get_object_or_404(University, pk=pk)
    if request.method == "POST":
        university.delete()
        return redirect("university_list")
    return render(request, "main/university_confirm_delete.html", {"university": university})


def student_list(request):
    students = Student.objects.select_related("university")
    return render(request, "main/student_list.html", {"students": students})


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "main/student_form.html", {"form": form})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)
    return render(request, "main/student_form.html", {"form": form})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    return render(request, "main/student_confirm_delete.html", {"student": student})
