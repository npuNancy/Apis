import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from specificApis import models, function
# Create your views here.


def login(request):
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def changePass(request):
    if not function.check_Session(request):
        return login(request)
    return render(request, 'changePass.html')


def signIn(request):
    if not function.check_Session(request):
        return login(request)
    return render(request, 'signIn.html')


def manageClass(request):
    if not function.check_Session(request):
        return login(request)
    return render(request, 'manageClass.html')


def studentEdit(request):
    if not function.check_Session(request):
        return login(request)
    if 'studentId' in request.GET:
        studentId = request.GET['studentId']
    return render(request, 'studentEdit.html', {'studentId': studentId})


def studentAdd(request):
    if not function.check_Session(request):
        return login(request)
    return render(request, 'studentAdd.html')


def classes(request):
    if not function.check_Session(request):
        return login(request)
    if 'classNumber' in request.GET:
        classNumber = request.GET['classNumber']
        return render(request, 'classes.html', {'classNumber': classNumber})
    else:
        return index(request)


def student(request):
    if not function.check_Session(request):
        return login(request)
    if 'studentId' in request.GET:
        studentId = request.GET['studentId']
        return render(request, 'student.html', {'studentId': studentId})
    else:
        return index(request)
