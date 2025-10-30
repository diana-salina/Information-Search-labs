from django.db import models


class University(models.Model):
    full_name = models.CharField("Полное название", max_length=255)
    short_name = models.CharField("Сокращённое название", max_length=50)
    foundation_date = models.DateField("Дата создания")

    def __str__(self):
        return self.short_name


class Student(models.Model):
    full_name = models.CharField("ФИО", max_length=255)
    birth_date = models.DateField("Дата рождения")
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="students")
    admission_year = models.PositiveIntegerField("Год поступления")

    def __str__(self):
        return self.full_name