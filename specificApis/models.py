from django.db import models

# Create your models here.


class Administrator(models.Model):
    username = models.CharField(max_length=20, db_index=True, unique=True)
    password = models.CharField(max_length=100, blank=False)


class GradeAdmin(models.Model):
    username = models.CharField(max_length=20, db_index=True, unique=True)
    password = models.CharField(max_length=100, blank=False)
    grade = models.ForeignKey(
        'Grade', to_field='grade', on_delete=models.PROTECT, null=True)


class Grade(models.Model):
    grade = models.CharField(max_length=20, db_index=True, unique=True)
    college = models.CharField(max_length=20, db_index=True)


class Classes(models.Model):
    grade = models.ForeignKey(
        'Grade', to_field='grade', on_delete=models.CASCADE)
    classNumber = models.OneToOneField(
        'User', to_field='classNumber', on_delete=models.CASCADE)


class User(models.Model):
    username = models.CharField(max_length=20, db_index=True, unique=True)
    password = models.CharField(max_length=100, blank=False)
    classNumber = models.CharField(max_length=20, db_index=True, unique=True)


class Student(models.Model):
    studentId = models.CharField(max_length=20, db_index=True, unique=True)
    name = models.CharField(max_length=20, db_index=True)
    sex = models.IntegerField(default=0)
    state = models.IntegerField(default=0)
    initPoints = models.DecimalField(
        max_digits=10, decimal_places=5, default=0)
    classNumber = models.ForeignKey(
        'Classes', to_field='classNumber', on_delete=models.CASCADE)


class StudentData(models.Model):
    studentId = models.ForeignKey(
        'Student', to_field='studentId', on_delete=models.CASCADE, null=True)
    state = models.IntegerField(default=0)
    points = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    duration = models.IntegerField(default=0)
    startTime = models.DateTimeField(auto_now_add=True)
    endTime = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now_add=True)
