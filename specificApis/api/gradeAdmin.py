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
