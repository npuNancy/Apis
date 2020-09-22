import json
import pytz
from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from specificApis.models import *
from specificApis import function


def retJson(obj=None, mycls=json.JSONEncoder, **kwargs):
    return HttpResponse(json.dumps(kwargs if obj is None else obj, cls=mycls), content_type='application/json')


@csrf_exempt
def test(request):
    """
    @api {post} /specificApis/test test
    @apiVersion 1.0.0
    @apiDescription test
    @apiName test
    @apiGroup test
    @apiParam {string} username username unique
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
    try:
        tes = StudentData.objects.filter(id='1').values()
        dbTime = tes[0]['date']
        dateToday = date.today() + timedelta(days=-1)
        a = StudentData.objects.filter(
            studentId='2018302275', date=dateToday).values()
        print(a)
        print(a[0])
        return retJson(values=a[0], mycls=function.MyEncoder)
    except Exception as e:
        return retJson(error=2, reason=str(e))


@csrf_exempt
def login(request):
    pass


@csrf_exempt
def logout(request):
    pass


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

        password = function.hash(password)
        try:
            user_Account = User(username=username,
                                password=password,
                                classNumber=classNumber)
            user_Account.save()
            try:
                gradeAccount = Grade.objects.get(grade=grade)
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
    @apiParam {string} username username unique
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
    if request.method == "POST":
        username = request.POST.get('username')
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
    if request.method == "POST":
        studentId = request.POST.get('studentId')
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        classNumber = request.POST.get('classNumber')
        if function.checkExist_student(studentId):
            try:
                class_Account = Classes.objects.get(classNumber=classNumber)
                student_Account__ = Student(classNumber=class_Account, sex=sex,
                                            studentId=studentId, name=name)
                student_Account__.save()
                return retJson(error=0, result="create student success")
            except Exception as e:
                return retJson(error=3, reason=str(e))
        else:
            return retJson(error=2, reason='Students dont exist')
    else:
        return retJson(error=1, reason='needmethod: post')


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
    if request.method == "GET":
        value = list(Student.objects.all().values())
        return retJson(error=0, result=value)
    else:
        return retJson(error=1, reason='needmethod: get')


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
    if request.method == "POST":
        studentId = request.POST.get('studentId')
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        classNumber = request.POST.get('classNumber')
        if function.checkExist_student(studentId):
            try:
                class_Account = Classes.objects.get(classNumber=classNumber)
                stud = Student.objects.filter(studentId=studentId)
                stud.update(classNumber=class_Account, name=name, sex=sex)
                return retJson(error=0, result="change student success")
            except Exception as e:
                return retJson(error=3, reason=str(e))
        else:
            return retJson(error=2, reason='Students dont exist')
    else:
        return retJson(error=1, reason='needmethod: post')


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
    if request.method == "POST":
        studentId = request.POST.get('studentId')
        if function.checkExist_student(studentId):
            try:
                Student.objects.filter(studentId=studentId).delete()
                return retJson(error=0, result="delete student success")
            except Exception as e:
                return retJson(error=3, reason=str(e))
        else:
            return retJson(error=2, reason='Students dont exist')
    else:
        return retJson(error=1, reason='needmethod: post')


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
    if request.method == "POST":
        # check if the # correct Time
        nowTime = datetime.strptime(
            datetime.now().strftime('%H:%M:%S'), '%H:%M:%S')
        config = function.config()
        earliestTime = datetime.strptime(config.startTime, '%H:%M:%S')
        latestTime = datetime.strptime(config.endTime, '%H:%M:%S')
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
                            return retJson(error=0, result='sign in success', values=values, mycls=function.MyEncoder)
                        except Exception as e:
                            return retJson(error=6, reason=str(e))
                    else:
                        return retJson(error=5, reason='not over yet')
                else:
                    return retJson(error=4, reason='has asked for leave')
            else:
                return retJson(error=3, reason='Students dont exist')
        else:
            # incorrect time
            return retJson(error=2, reason='incorrect time')
    else:
        return retJson(error=1, reason='needmethod: post')


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
    if request.method == 'POST':
        studentId = request.POST.get('studentId')
        dataId = request.POST.get('dataId')
        dateToday = date.today()
        if function.checkExist_student(studentId):
            try:
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
                    return retJson(error=0, result='sign out success', values=values, mycls=function.MyEncoder)
                else:
                    return retJson(error=4, reason='wrong state')
            except Exception as e:
                return retJson(error=3, reason=str(e))
        else:
            return retJson(error=2, reason='Students dont exist')
    else:
        return retJson(error=1, reason='needmethod: POST')


@csrf_exempt
def askLeave(request):
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
    if request.method == "POST":
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
                            studentId=student_Account, state=1)
                        obje_Data.save()
                        values = StudentData.objects.filter(
                            studentId=student_Account, date=dateToday, state=1).values()[0]
                        return retJson(error=0, values=values, mycls=function.MyEncoder)
                    except Exception as e:
                        return retJson(error=6, reason=str(e))
                else:
                    return retJson(error=5, reason='not over yet')
            else:
                return retJson(error=4, reason='has asked for leave')
        else:
            return retJson(error=2, reason='Students dont exist')
    else:
        return retJson(error=1, reason='needmethod: post')
