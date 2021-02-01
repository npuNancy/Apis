import json
import os
from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from specificApis.models import *
from specificApis import function


@csrf_exempt
def studentAdd(request):
    """
    @api {post} /specificApis/student/add studentAdd
    @apiVersion 1.0.0
    @apiDescription studentAdd
    @apiName studentAdd
    @apiGroup student
    @apiParam {string} studentId studentId unique
    @apiParam {string} name name
    @apiParam {int} sex sex
    @apiParam {int} state state
    @apiParam {int} initPoints initial points
    @apiParam {string} classNumber classNumber 外键
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "create student success"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    if not function.check_Session(request):
        return function.retJson(error=-1, reason='have not login')
    if request.method == "POST":
        studentId = request.POST.get('studentId')
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        state = request.POST.get('state')
        initPoints = request.POST.get('initPoints')
        classNumber = request.POST.get('classNumber')
        try:
            class_Account = Classes.objects.get(classNumber=classNumber)
            student_Account__ = Student(classNumber=class_Account, sex=sex,
                                        studentId=studentId, name=name,
                                        state=state, initPoints=initPoints)
            student_Account__.save()
            return function.retJson(error=0, result="create student success")
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=1, reason='needmethod: post')


@csrf_exempt
def studentGet(request):
    """
    @api {get} /specificApis/student/get studentGet
    @apiVersion 1.0.0
    @apiDescription studentGet
    @apiName studentGet
    @apiGroup student
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": value
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    if not function.check_Session(request) and not function.check_gradeAdminSession(request):
        return function.retJson(error=-1, reason='have not login')
    if request.method == "GET":
        value = list(Student.objects.all().values())
        return function.retJson(error=0, result=value, mycls=function.MyEncoder)
    else:
        return function.retJson(error=1, reason='needmethod: get')


@csrf_exempt
def studentChange(request):
    """
    @api {post} /specificApis/student/change studentChange
    @apiVersion 1.0.0
    @apiDescription studentChange
    @apiName studentChange
    @apiGroup student
    @apiParam {string} studentId studentId unique
    @apiParam {string} name name
    @apiParam {int} sex sex
    @apiParam {string} classNumber classNumber 外键
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": change student success
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    if not function.check_Session(request):
        return function.retJson(error=-1, reason='have not login')
    if request.method == "POST":
        studentId = request.POST.get('studentId')
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        sex = 1 if(sex == "男") else 0
        initPoints = request.POST.get('initPoints')
        print(studentId)
        # classNumber = request.POST.get('classNumber')
        if function.checkExist_student(studentId):
            try:
                stud = Student.objects.filter(studentId=studentId)
                stud.update(name=name, sex=sex, initPoints=initPoints)
                # class_Account = Classes.objects.get(classNumber=classNumber)
                # stud.update(classNumber=class_Account, name=name, sex=sex)
                return function.retJson(error=0, result="change student success")
            except Exception as e:
                return function.retJson(error=3, reason=str(e))
        else:
            return function.retJson(error=2, reason='Students dont exist')
    else:
        return function.retJson(error=1, reason='needmethod: post')


@csrf_exempt
def studentDelete(request):
    """
    @api {post} /specificApis/student/delete studentDelete
    @apiVersion 1.0.0
    @apiDescription Delete student
    @apiName studentDelete
    @apiGroup student
    @apiParam {string} studentId studentId unique
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "delete student success"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    if not function.check_Session(request):
        return function.retJson(error=-1, reason='have not login')
    if request.method == "POST":
        studentId = request.POST.get('studentId')
        if function.checkExist_student(studentId):
            try:
                Student.objects.filter(studentId=studentId).delete()
                return function.retJson(error=0, result="delete student success")
            except Exception as e:
                return function.retJson(error=3, reason=str(e))
        else:
            return function.retJson(error=2, reason='Students dont exist')
    else:
        return function.retJson(error=1, reason='needmethod: post')
