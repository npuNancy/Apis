import json
import os
from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from specificApis.models import *
from specificApis import function

import json


@csrf_exempt
def getUsername(request):
    """
    @api {get} /specificApis/user/getUsername getUsername
    @apiVersion 1.0.0
    @apiDescription get username
    @apiName getUsername
    @apiGroup user
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "get username success"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    if not function.check_Session(request):
        return retJson(error=-1, reason='have not login')
    username = request.session.get('username')
    return retJson(error=0, result=username)


@csrf_exempt
def getUserClassNumber(request):
    """
    @api {get} /specificApis/user/getUserClassNumber getUserClassNumber
    @apiVersion 1.0.0
    @apiDescription getUserClassNumber
    @apiName getUserClassNumber
    @apiGroup user
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "get UserClassNumber success"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    if not function.check_Session(request):
        return retJson(error=-1, reason='have not login')
    try:
        username = request.session.get('username')
        classNumber = User.objects.filter(username=username).values()[
            0]['classNumber']
        return retJson(error=0, classNumber=classNumber)
    except Exception as e:
        return retJson(error=1, reason=str(e))


@csrf_exempt
def userAdd(request):
    """
    @api {post} /specificApis/user/add userAdd
    @apiVersion 1.0.0
    @apiDescription userAdd
    @apiName userAdd
    @apiGroup user
    @apiParam {string} username username unique
    @apiParam {string} password password
    @apiParam {string} classNumber classNumber unique
    @apiParam {string} grade grade
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "create user success"
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
        classNumber = request.POST.get('classNumber')
        grade = request.POST.get('grade')
        # TODO password decode
        password = function.hash(password)
        try:
            gradeAccount = Grade.objects.get(grade=grade)
            user_Account = User(username=username,
                                password=password,
                                classNumber=classNumber)
            user_Account.save()
            try:
                class_Account = Classes(classNumber=user_Account,
                                        grade=gradeAccount)
                class_Account.save()
                return retJson(error=0, result="create user success")
            except Exception as e:
                return retJson(error=1, reason=str(e))
        except Exception as e:
            return retJson(error=2, reason=str(e))
    else:
        return retJson(error=3, reason='needmethod: post')


@csrf_exempt
def userChangePass(request):
    """
    @api {post} /specificApis/user/changePass userChangePass
    @apiVersion 1.0.0
    @apiDescription change user's password
    @apiName userChangePass
    @apiGroup user
    @apiParam {string} password new password
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "create user success"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    if not function.check_Session(request):
        return retJson(error=-1, reason='have not login')
    if request.method == "POST":
        username = request.session.get('username')
        password = request.POST.get('password')

        password = function.hash(password)
        try:
            user_Account = User.objects.filter(username=username)
            user_Account.update(password=password)
            return retJson(error=0, result="change user's password success")
        except Exception as e:
            return retJson(error=2, reason=str(e))
    else:
        return retJson(error=3, reason='needmethod: post')


@csrf_exempt
def checkPass(request):
    """
    @api {post} /specificApis/user/checkPass checkPass
    @apiVersion 1.0.0
    @apiDescription checkPass
    @apiName checkPass
    @apiGroup user
    @apiParam {string} password password
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "login"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    if request.method == "POST":
        password = request.POST.get('password')
        username = request.session.get('username')
        try:
            password = function.hash(password)
            if function.check_UserPass(username, password):
                return retJson(error=0, result='check password success')
            else:
                return retJson(error=3, reason='wrong password')
        except Exception as e:
            return retJson(error=2, reason=str(e))
    else:
        return retJson(error=1, reason='please use post')


@csrf_exempt
def login(request):
    """
    @api {post} /specificApis/login/login login
    @apiVersion 1.0.0
    @apiDescription login
    @apiName login
    @apiGroup user
    @apiParam {string} username username unique
    @apiParam {string} password password
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "login"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            password = function.hash(password)
            if function.check_UserPass(username, password):
                request.session['is_login'] = True
                request.session['username'] = username
                return retJson(error=0, result='login')
            else:
                return retJson(error=3, reason='wrong username or password')
        except Exception as e:
            return retJson(error=2, reason=str(e))
    else:
        return retJson(error=1, reason='wrong method')


@csrf_exempt
def logout(request):
    """
    @api {get} /specificApis/login/logout logout
    @apiVersion 1.0.0
    @apiDescription logout
    @apiName logout
    @apiGroup user
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
        if not function.check_Session(request):
            return retJson(error=-1, reason='have not login')
        request.session.flush()
        return retJson(error=0, resule='logout')
    except Exception as e:
        return retJson(error=1, reason=str(e))
