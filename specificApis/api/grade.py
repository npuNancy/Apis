import json
import os
from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from specificApis.models import *
from specificApis import function


@csrf_exempt
def gradeGetAll(request):
    """
    @api {get} /specificApis/grade/gradeGetAll gradeGetAll
    @apiVersion 1.0.0
    @apiDescription get All grade
    @apiName gradeGetAll
    @apiGroup grade
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "{"grade": admin2018, "college": "2018"}"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    try:
        grade = list(Grade.objects.filter().values())
        return function.retJson(error=0, result=grade)
    except Exception as e:
        return function.retJson(error=3, reason=str(e))


@csrf_exempt
def gradeAdd(request):
    """
    @api {POST} /specificApis/grade/gradeAdd gradeAdd
    @apiVersion 1.0.0
    @apiDescription add a grade
    @apiName gradeAdd
    @apiGroup grade
    @apiParam {string} grade grade
    @apiParam {string} college college
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "create grade success"
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
            grade = request.POST.get('grade')
            college = request.POST.get('college')
            gradeAccount = Grade(grade=grade, college=college)
            gradeAccount.save()
            return function.retJson(error=0, result="create grade success")
        except Exception as e:
            return function.retJson(error=3, reason=str(e))
    else:
        return function.retJson(error=1, reason='need method: post')


@csrf_exempt
def gradeDelete(request):
    """
    @api {POST} /specificApis/grade/gradeDelete gradeDelete
    @apiVersion 1.0.0
    @apiDescription delete a grade
    @apiName gradeDelete
    @apiGroup grade
    @apiParam {string} gradeId gradeId
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "delete grade success"
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
            gradeId = request.POST.get('gradeId')
            Grade.objects.get(id=gradeId).delete()
            return function.retJson(error=0, result="delete grade success")
        except Exception as e:
            return function.retJson(error=3, reason=str(e))
    else:
        return function.retJson(error=1, reason='need method: post')
