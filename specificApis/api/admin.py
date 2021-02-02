import json
import os
from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from specificApis.models import *
from specificApis import function


@csrf_exempt
def login(request):
    """
    @api {post} /specificApis/admin/login login
    @apiVersion 1.0.0
    @apiDescription 系统管理员和年级管理员 登录
    @apiName login
    @apiGroup admin
    @apiParam {string} username username unique
    @apiParam {string} password password
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "grade admin" or "admin"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            request.session.flush()
            password = function.hash(password)
            res_admin = function.check_adminPass(username, password)
            res_grade = function.check_gradeAdminPass(username, password)
            if res_admin:
                request.session['is_login_admin'] = True
                request.session['username_admin'] = username
                return function.retJson(error=0, result='admin login success', types='admin')
            elif res_grade:
                request.session['is_login_grade'] = True
                request.session['username_grade'] = username
                return function.retJson(error=0, result='grade admin login success', types='grade')
            else:
                return function.retJson(error=3, reason='wrong username or password')
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=1, reason='wrong method')


@csrf_exempt
def logout(request):
    """
    @api {get} /specificApis/admin/logout logout
    @apiVersion 1.0.0
    @apiDescription 系统管理员退出登录
    @apiName logout
    @apiGroup admin
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
        if not function.check_adminSession(request):
            return function.retJson(error=-1, reason='have not login')
        request.session.flush()
        return function.retJson(error=0, resule='logout')
    except Exception as e:
        return function.retJson(error=1, reason=str(e))


@csrf_exempt
def checkPass(request):
    """
    @api {post} /specificApis/admin/checkPass checkPass
    @apiVersion 1.0.0
    @apiDescription 修改密码时检查原密码正确性
    @apiName checkPass
    @apiGroup admin
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
    if not function.check_adminSession(request):
        return function.retJson(error=-1, reason='have not login')
    if request.method == "POST":
        try:
            username = request.session.get('username_admin')
            password = request.POST.get('password')
            password = function.hash(password)
            if function.check_adminPass(username, password):
                return function.retJson(error=0, result='check password success')
            else:
                return function.retJson(error=3, reason='wrong password')
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=1, reason='please use post')


@csrf_exempt
def changePass(request):
    """
    @api {post} /specificApis/admin/changePass changePass
    @apiVersion 1.0.0
    @apiDescription 修改密码
    @apiName changePass
    @apiGroup admin
    @apiParam {string} password password
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "change admin's password success"
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
        password = request.POST.get('password')
        username = request.session.get('username_admin')
        password = function.hash(password)
        try:
            admin_Account = Administrator.objects.filter(username=username)
            admin_Account.update(password=password)
            return function.retJson(error=0, result="change admin's password success")
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=3, reason='needmethod: post')


@csrf_exempt
def adminAdd(request):
    """
    @api {post} /specificApis/admin/add adminAdd
    @apiVersion 1.0.0
    @apiDescription adminAdd
    @apiName adminAdd
    @apiGroup admin
    @apiParam {string} username username unique
    @apiParam {string} password password
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
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password = function.hash(password)
        try:
            admin_Account = Administrator(
                username=username, password=password)
            admin_Account.save()
            return function.retJson(error=0, result="create admin success")

        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=3, reason='need method: post')


@csrf_exempt
def getConfig(request):
    """
    @api {get} /specificApis/admin/getConfig getConfig
    @apiVersion 1.0.0
    @apiDescription 查看开始结束时间、要求时长等配置信息
    @apiName getConfig
    @apiGroup admin
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "{'startTime':'xxx', ……}"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    try:
        if not function.check_adminSession(request):
            return function.retJson(error=-1, reason='have not login')

        conf = Config.objects.get(name='default')
        rets = {'startTime': str(conf.startTime),
                'endTime': str(conf.endTime),
                'requiredPoints': conf.requiredPoints,
                'pointsPerHour': conf.pointsPerHour}
        return function.retJson(error=0, result=rets)
    except Exception as e:
        return function.retJson(error=1, reason=str(e))


@csrf_exempt
def editConfig(request):
    """
    @api {post} /specificApis/admin/editConfig editConfig
    @apiVersion 1.0.0
    @apiDescription 修改开始结束时间、要求时长等配置信息
    @apiName editConfig
    @apiGroup admin
    @apiParam {string} username username unique
    @apiParam {string} password password
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "edit config success"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    try:
        if not function.check_adminSession(request):
            return function.retJson(error=-1, reason='have not login')
        if request.method == "POST":
            conf = Config.objects.get(name='default')
            conf.endTime = request.POST.get('endTime')
            conf.startTime = request.POST.get('startTime')
            conf.requiredPoints = request.POST.get('requiredPoints')
            # conf.pointsPerHour = request.POST.get('pointsPerHour')
            conf.save()
            return function.retJson(error=0, resule="edit config success")
        else:
            return function.retJson(error=3, reason='needmethod: post')
    except Exception as e:
        return function.retJson(error=1, reason=str(e))
