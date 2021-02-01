import json
import os
from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from specificApis.models import *
from specificApis import function


@csrf_exempt
def gradeAdminAdd(request):
    """
    @api {post} /specificApis/gradeAdmin/gradeAdminAdd gradeAdminAdd
    @apiVersion 1.0.0
    @apiDescription add grade admin
    @apiName gradeAdminAdd
    @apiGroup gradeAdmin
    @apiParam {string} username username unique
    @apiParam {string} password password
    @apiParam {string} gradeId gradeId
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "create admin success"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    if not function.check_adminSession(request):
        return function.retJson(error=-1, reason='have not login')
    if request.method == "POST":
        username = request.POST.get('username')
        gradeId = request.POST.get('gradeId')
        password = request.POST.get('password')
        password = function.hash(password)
        try:
            gradeInfo = Grade.objects.get(id=gradeId)
            admin_Account = GradeAdmin(
                username=username, password=password, grade=gradeInfo)
            admin_Account.save()
            return function.retJson(error=0, result="create grade admin success")
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=3, reason='need method: post')


@ csrf_exempt
def gradeAdminDelete(request):
    """
    @api {post} /specificApis/gradeAdmin/gradeAdminDelete gradeAdminDelete
    @apiVersion 1.0.0
    @apiDescription delete gradeAdmin
    @apiName gradeAdminDelete
    @apiGroup gradeAdmin
    @apiParam {string} username grade admin username
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "delete admin success"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    if not function.check_adminSession(request):
        return function.retJson(error=-1, reason='have not login')
    if request.method == "POST":
        username = request.POST.get('username')
        try:
            GradeAdmin.objects.get(username=username).delete()
            return function.retJson(error=0, result="delete grade admin success")
        except Exception as e:
            return function.retJson(error=3, reason=str(e))
    else:
        return function.retJson(error=1, reason='need method: post')


@ csrf_exempt
def gradeAdminGetAll(request):
    """
    @api {get} /specificApis/gradeAdmin/gradeAdminGetAll gradeAdminGetAll
    @apiVersion 1.0.0
    @apiDescription get All gradeAdmin
    @apiName gradeAdminGetAll
    @apiGroup gradeAdmin
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "{"username": admin2018, "grade": "2018"}"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    if not function.check_adminSession(request):
        return function.retJson(error=-1, reason='have not login')
    try:
        gradeAdminList = list(
            GradeAdmin.objects.filter().values())
        for gradeAdmin in gradeAdminList:
            gradeAdmin.pop("id")
            gradeAdmin.pop("password")
        return function.retJson(error=0, result=gradeAdminList)
    except Exception as e:
        return function.retJson(error=3, reason=str(e))


@csrf_exempt
def gradeAdminLogout(request):
    """
    @api {get} /specificApis/gradeAdmin/gradeAdminLogout gradeAdminLogout
    @apiVersion 1.0.0
    @apiDescription 年级管理员退出登录
    @apiName gradeAdminLogout
    @apiGroup gradeAdmin
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "logout"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    try:
        if not function.check_gradeAdminSession(request):
            return function.retJson(error=-1, reason='have not login')
        request.session.flush()
        return function.retJson(error=0, resule='logout')
    except Exception as e:
        return function.retJson(error=1, reason=str(e))


@csrf_exempt
def GAcheckPass(request):
    """
    @api {post} /specificApis/gradeAdmin/GAcheckPass GAcheckPass
    @apiVersion 1.0.0
    @apiDescription 修改密码时检查原密码正确性
    @apiName GAcheckPass
    @apiGroup gradeAdmin
    @apiParam {string} password password
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "check password success"
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
    if request.method == "POST":
        try:
            username = request.session.get('username_grade')
            password = request.POST.get('password')
            password = function.hash(password)
            if function.check_gradeAdminPass(username, password):
                return function.retJson(error=0, result='check password success')
            else:
                return function.retJson(error=3, reason='wrong password')
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=1, reason='please use post')


@csrf_exempt
def GAchangePass(request):
    """
    @api {post} /specificApis/gradeAdmin/GAchangePass GAchangePass
    @apiVersion 1.0.0
    @apiDescription 修改密码
    @apiName GAchangePass
    @apiGroup gradeAdmin
    @apiParam {string} password_new password_new
    @apiParam {string} password_old password_old
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "change grade_admin's password success"
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
    if request.method == "POST":
        try:
            username = request.session.get('username_grade')
            password_new = request.POST.get('password_new')
            password_new = function.hash(password_new)
            password_old = request.POST.get('password_old')
            password_old = function.hash(password_old)

            if not function.check_gradeAdminPass(username, password_old):
                return function.retJson(error=3, reason='wrong password')
            else:
                admin_Account = GradeAdmin.objects.filter(username=username)
                admin_Account.update(password=password_new)
                return function.retJson(error=0, result="change grade_admin's password success")
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=1, reason='needmethod: post')


@csrf_exempt
def GAgetClasses(request):
    """
    @api {get} /specificApis/gradeAdmin/GAgetClasses GAgetClasses
    @apiVersion 1.0.0
    @apiDescription 获取当前年级管理员管理的年级下的所有班级
    @apiName GAgetClasses
    @apiGroup gradeAdmin
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": ""
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
            username = request.session.get('username_grade')
            grade = GradeAdmin.objects.get(username=username).grade.grade
            classes = list(Classes.objects.filter(grade=grade).values())
            users = []
            for item in classes:
                info = item['classNumber_id']
                userInfo = list(User.objects.filter(classNumber=info).values())
                users.append({'user': userInfo[0]['username'], 'class': info})
            return function.retJson(error=0, classes=classes, users=users, grade=grade, mycls=function.MyEncoder)
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=1, reason='needmethod: get')


@csrf_exempt
def GAclassAdd(request):
    """
    @api {post} /specificApis/gradeAdmin/GAclassAdd GAclassAdd
    @apiVersion 1.0.0
    @apiDescription 添加班级，并将会创建一个默认班级负责人，此管理员用户名和初始密码与班号相同。
    @apiName GAclassAdd
    @apiGroup gradeAdmin
    @apiParam {string} classNumber classNumber
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "create class and user success"
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
    if request.method == "POST":
        try:
            grade = GradeAdmin.objects.get(
                username=request.session.get('username_grade')).grade.grade
            classNumber = request.POST.get('classNumber')
            username = classNumber
            password = classNumber
            password = function.hash(password)

            gradeAccount = Grade.objects.get(grade=grade)
            user_Account = User(username=username,
                                password=password,
                                classNumber=classNumber)
            user_Account.save()
            try:
                class_Account = Classes(classNumber=user_Account,
                                        grade=gradeAccount)
                class_Account.save()
                return function.retJson(error=0, result="create class and user success")
            except Exception as e:
                return function.retJson(error=1, reason=str(e))
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=3, reason='needmethod: post')


@csrf_exempt
def GAclassDelete(request):
    """
    @api {post} /specificApis/gradeAdmin/GAclassDelete GAclassDelete
    @apiVersion 1.0.0
    @apiDescription 删除班级,班级有同学的时候，拒绝删除
    @apiName GAclassDelete
    @apiGroup gradeAdmin
    @apiParam {string} classNumber classNumber
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "delete class success"
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
    if request.method == "POST":
        try:
            classNumber = request.POST.get('classNumber')
            Classes.objects.get(classNumber=classNumber).delete()
            return function.retJson(error=0, result="delete class success")
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=1, reason='needmethod: get')
