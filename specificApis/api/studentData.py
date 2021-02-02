import json
import os
from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from specificApis.models import *
from specificApis import function


@csrf_exempt
def signIn(request):
    """
    @api {post} /specificApis/studentData/signIn signIn
    @apiVersion 1.0.0
    @apiDescription 开始签到
    @apiName signIn
    @apiGroup studentData
    @apiParam {string} studentId studentId unique
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "Record success"
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
        try:
            # check if the # correct Time
            nowTime = datetime.strptime(
                datetime.now().strftime('%H:%M:%S'), '%H:%M:%S')
            conf = Config.objects.get(name='default')
            earliestTime = datetime.strptime(str(conf.startTime), '%H:%M:%S')
            latestTime = datetime.strptime(str(conf.startTime), '%H:%M:%S')
            if nowTime >= earliestTime and nowTime <= latestTime:
                # correct time
                studentId = request.POST.get('studentId')
                dateToday = date.today()
                if function.checkExist_student(studentId):
                    student_Account = Student.objects.get(
                        studentId=studentId)
                    flag_askLeave = StudentData.objects.filter(
                        studentId=student_Account, date=dateToday, state=1)
                    if not flag_askLeave:
                        flag_notOver = StudentData.objects.filter(
                            studentId=student_Account, date=dateToday, state=2)
                        if not flag_notOver:
                            try:
                                obje_Data = StudentData(
                                    studentId=student_Account, state=2)
                                obje_Data.save()
                                values = StudentData.objects.filter(
                                    studentId=student_Account, date=dateToday, state=2).values()[0]
                                return function.retJson(error=0, result='sign in success', values=values, mycls=function.MyEncoder)
                            except Exception as e:
                                return function.retJson(error=6, reason=str(e))
                        else:
                            return function.retJson(error=5, reason='not over yet')
                    else:
                        return function.retJson(error=4, reason='has asked for leave')
                else:
                    return function.retJson(error=3, reason='Students dont exist')
            else:
                # incorrect time
                return function.retJson(error=2, reason='incorrect time')
        except Exception as e:
            return function.retJson(error=6, reason=str(e))

    else:
        return function.retJson(error=1, reason='needmethod: post')


@csrf_exempt
def signOut(request):
    """
    @api {post} /specificApis/studentData/signOut signOut
    @apiVersion 1.0.0
    @apiDescription sign Out
    @apiName signOut
    @apiGroup studentData
    @apiParam {string} studentId studentId unique
    @apiParam {string} dataId dataId unique
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "sign Out success"
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
    if request.method == 'POST':
        try:
            studentId = request.POST.get('studentId')
            dataId = request.POST.get('dataId')
            dateToday = date.today()
            if function.checkExist_student(studentId):
                data = StudentData.objects.get(id=dataId)
                if data.state == 2:
                    data.state = 3
                    data.save()
                    data = StudentData.objects.filter(id=dataId)
                    startTime = data.values()[0]['startTime']
                    endTime = data.values()[0]['endTime']
                    duration = function.calDurationTime(startTime, endTime)[0]
                    points = function.calDurationTime(startTime, endTime)[1]
                    data.update(duration=duration, points=points)
                    values = StudentData.objects.filter(id=dataId).values()[0]
                    return function.retJson(error=0, result='sign out success', values=values, mycls=function.MyEncoder)
                else:
                    return function.retJson(error=4, reason='wrong state')
            else:
                return function.retJson(error=2, reason='Students dont exist')
        except Exception as e:
            return function.retJson(error=3, reason=str(e))
    else:
        return function.retJson(error=1, reason='needmethod: POST')


@csrf_exempt
def askLeave(request):
    # will not use
    """
    @api {post} /specificApis/studentData/askLeave askLeave
    @apiVersion 1.0.0
    @apiDescription ask for leave
    @apiName askLeave
    @apiGroup studentData
    @apiParam {string} studentId studentId unique
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "ask for leave success"
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
        dateToday = date.today()
        if function.checkExist_student(studentId):
            # 学生存在
            student_Account = Student.objects.get(
                studentId=studentId)
            flag_askLeave = StudentData.objects.filter(
                studentId=student_Account, date=dateToday, state=1)
            if not flag_askLeave:
                # 今天没请过假
                flag_notOver = StudentData.objects.filter(
                    studentId=student_Account, date=dateToday, state=2)
                if not flag_notOver:
                    # 还没结束
                    flag_notStart = StudentData.objects.filter(
                        studentId=student_Account, date=dateToday, state=3)
                    if not flag_notStart:
                        # 还没开始过
                        try:
                            obje_Data = StudentData(
                                studentId=student_Account, state=1, points=0)  # 请假/不来 0 积分
                            obje_Data.save()
                            values = StudentData.objects.filter(
                                studentId=student_Account, date=dateToday, state=1).values()[0]
                            return function.retJson(error=0, values=values, mycls=function.MyEncoder)
                        except Exception as e:
                            return function.retJson(error=7, reason=str(e))
                    else:
                        # 开始过
                        return function.retJson(error=6, reason='cant ask for leave')
                else:
                    return function.retJson(error=5, reason='not over yet')
            else:
                return function.retJson(error=4, reason='has asked for leave')
        else:
            return function.retJson(error=2, reason='Students dont exist')
    else:
        return function.retJson(error=1, reason='needmethod: post')


@csrf_exempt
def getStudentStates(request):
    """
    @api {post} /specificApis/studentData/getStudentstates getStudentStates
    @apiVersion 1.0.0
    @apiDescription getStudentStates
    @apiName getStudentStates
    @apiGroup studentData
    @apiParam {string} studentId studentId unique
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "ask for leave success"
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
        dateToday = date.today()
        try:
            if function.checkExist_student(studentId):
                # student exist
                student_Account = Student.objects.get(
                    studentId=studentId)
                flag_askLeave = StudentData.objects.filter(
                    studentId=student_Account, date=dateToday, state=1)
                if not flag_askLeave:
                    # 今日还没请假
                    flag_notOver = StudentData.objects.filter(
                        studentId=student_Account, date=dateToday, state=2)
                    if not flag_notOver:
                        flag_notStart = StudentData.objects.filter(
                            studentId=student_Account, date=dateToday, state=3)
                        if not flag_notStart:
                            return function.retJson(error=0, state=0)
                        else:
                            # 今天开始过
                            st = flag_notStart.values()[0]['startTime'].strftime(
                                '%Y-%m-%d %H:%M:%S')
                            et = flag_notStart.values()[0]['endTime'].strftime(
                                '%Y-%m-%d %H:%M:%S')
                            points = flag_notStart.values()[0]['points']
                            return function.retJson(error=0, state=3, starttime=st, endtime=et, points=points,  mycls=function.MyEncoder)
                    else:
                        st = flag_notOver.values()[0]['startTime'].strftime(
                            '%Y-%m-%d %H:%M:%S')
                        dataId = flag_notOver.values()[0]['id']
                        # 没结束
                        return function.retJson(error=0, state=2, starttime=st, dataId=dataId)
                else:
                    return function.retJson(error=0, state=1)  # 请假
            else:
                return function.retJson(error=3, reason='Students dont exist')
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=1, reason='needmethod: post')


@csrf_exempt
def getClassStudents(request):
    """
    @api {get} /specificApis/studentData/getClassStudents getClassStudents
    @apiVersion 1.0.0
    @apiDescription get this class's students
    @apiName getClassStudents
    @apiGroup studentData
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "ask for leave success"
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
    if request.method == "GET":
        try:
            username = request.session.get('username')
            classNumber = User.objects.filter(username=username).values()[
                0]['classNumber']
            stu = Student.objects.filter(
                classNumber__classNumber=classNumber).values()
            return function.retJson(error=0, result=list(stu), mycls=function.MyEncoder)
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=1, reason='needmethod: get')


@csrf_exempt
def signOutCron(request):
    """
    @api {get} /specificApis/studentData/signOutCron signOutCron
    @apiVersion 1.0.0
    @apiDescription signOutCron
    @apiName signOutCron
    @apiGroup studentData
    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "error": 0,
            "result": "success"
        }
    @apiErrorExample {json} Error-Response:
        HTTP/1.1 200 OK
        {
            "error": 1,
            "reason": "error reason here"
        }
    """
    try:
        ret = function.cron_signOut()
        return function.retJson(error=0, result=ret)
    except Exception as e:
        return function.retJson(error=2, reason=str(e))
