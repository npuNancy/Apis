import json
import os
from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from specificApis.models import *
from specificApis import function


@csrf_exempt
def getStudentData(request):
    """
    @api {post} /specificApis/show/getStudentData getStudentData
    @apiVersion 1.0.0
    @apiDescription getStudentData
    @apiName getStudentData
    @apiGroup show
    @apiParam {string} studentId studentId unique
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "get all class info success"
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
    if request.method == "POST":
        try:
            studentId = request.POST.get('studentId')
            student, stuDatas = function.getStudentData(studentId)
            return function.retJson(error=0, student=student, data=list(stuDatas), mycls=function.MyEncoder)
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=1, reason='needmethod: post')


@csrf_exempt
def getClassData(request):
    """
    @api {post} /specificApis/show/getClassData getClassData
    @apiVersion 1.0.0
    @apiDescription getClassData
    @apiName getClassData
    @apiGroup show
    @apiParam {string} classNumber classNumber
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "get all class info success"
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
    if request.method == "POST":
        try:
            classNumber = request.POST.get('classNumber')
            classs, students = function.getClassData(classNumber)

            return function.retJson(error=0, classs=classs, data=list(students), mycls=function.MyEncoder)
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=1, reason='needmethod: get')


@csrf_exempt
def getAllClass(request):
    """
    @api {get} /specificApis/show/getAllClass getAllClass
    @apiVersion 1.0.0
    @apiDescription get all class info
    @apiName getAllClass
    @apiGroup show
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "get all class info success"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    if not function.check_gradeAdminSession(request):
        return function.retJson(error=-1, reason='have not login')
    if request.method == "GET":
        try:
            classes = Classes.objects.filter().values()
            people = 0
            requiredPeople = 0
            classInfo = []
            for cl in classes:
                classNumber = cl['classNumber_id']
                info = function.getClassData(classNumber)[0]
                people += info['number']
                requiredPeople += info['requiredPeople']
                classInfo.append(info)
            result = {
                'people': people,
                'requiredPeople': requiredPeople
            }
            return function.retJson(error=0, result=result, classInfo=classInfo, mycls=function.MyEncoder)
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=1, reason='needmethod: get')


@csrf_exempt
def getGradeClass(request):
    """
    @api {get} /specificApis/show/getGradeClass getGradeClass
    @apiVersion 1.0.0
    @apiDescription get one grades's all class info
    @apiName getGradeClass
    @apiGroup show
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "get class info success"
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
        try:
            if function.check_Session(request):
                username = request.session.get('username')
                classNum = User.objects.get(username=username).classNumber
                classes = Classes.objects.filter(classNumber=classNum).values()
                people = 0
                requiredPeople = 0
                classInfo = []
                for cl in classes:
                    classNumber = cl['classNumber_id']
                    info = function.getClassData(classNumber)[0]
                    people += info['number']
                    requiredPeople += info['requiredPeople']
                    classInfo.append(info)
                result = {
                    'people': people,
                    'requiredPeople': requiredPeople
                }
                return function.retJson(error=0, result=result, classInfo=classInfo, mycls=function.MyEncoder, role='user')

            elif function.check_gradeAdminSession(request):
                username = request.session.get('username_grade')
                grade = GradeAdmin.objects.get(username=username).grade.grade
                classes = Classes.objects.filter(grade=grade).values()
                people = 0
                requiredPeople = 0
                classInfo = []
                for cl in classes:
                    classNumber = cl['classNumber_id']
                    info = function.getClassData(classNumber)[0]
                    people += info['number']
                    requiredPeople += info['requiredPeople']
                    classInfo.append(info)
                result = {
                    'people': people,
                    'requiredPeople': requiredPeople
                }
                return function.retJson(error=0, result=result, classInfo=classInfo, mycls=function.MyEncoder, role='gradeAdmin')
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=1, reason='needmethod: get')
