import json
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from specificApis import models, function
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request, 'index.html', {"type": "user"})


def login(request):
    if function.check_Session(request):
        return HttpResponseRedirect("/index")
    return render(request, 'login.html', {"type": "user"})


def changePass(request):
    if not function.check_Session(request):
        return HttpResponseRedirect("/login")
    return render(request, 'changePass.html')


def signIn(request):
    if not function.check_Session(request):
        return HttpResponseRedirect("/login")
    return render(request, 'signIn.html')


def manageClass(request):
    if not function.check_Session(request):
        return HttpResponseRedirect("/login")
    return render(request, 'manageClass.html')


def studentEdit(request):
    if not function.check_Session(request):
        return HttpResponseRedirect("/login")
    if 'studentId' in request.GET:
        studentId = request.GET['studentId']
    return render(request, 'studentEdit.html', {'studentId': studentId})


def studentAdd(request):
    if not function.check_Session(request):
        return HttpResponseRedirect("/login")
    return render(request, 'studentAdd.html')


def classes(request):
    if not function.check_Session(request):
        return HttpResponseRedirect("/login")
    if 'classNumber' in request.GET:
        classNumber = request.GET['classNumber']
        return render(request, 'classes.html', {'classNumber': classNumber})
    else:
        return index(request)


def student(request):
    if not function.check_Session(request):
        return HttpResponseRedirect("/login")
    if 'studentId' in request.GET:
        studentId = request.GET['studentId']
        return render(request, 'student.html', {'studentId': studentId})
    else:
        return index(request)


def adminLogin(request):
    if function.check_adminSession(request):
        return HttpResponseRedirect("/adminIndex")
    if function.check_gradeAdminSession(request):
        return HttpResponseRedirect("/gradeAdminIndex")
    return render(request, 'login.html', {"type": "admin"})


def adminIndex(request):
    if not function.check_adminSession(request):
        return HttpResponseRedirect("/adminLogin")
    return render(request, 'adminIndex.html', {"type": "admin"})


def gradeAdminIndex(request):
    if not function.check_gradeAdminSession(request):
        return HttpResponseRedirect("/adminLogin")
    return render(request, 'gradeAdminIndex.html')
