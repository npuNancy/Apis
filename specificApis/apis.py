import json
import os
from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from specificApis.models import *
from specificApis import function


def retJson(obj=None, mycls=json.JSONEncoder, **kwargs):
    return HttpResponse(json.dumps(kwargs if obj is None else obj, cls=mycls), content_type='application/json')

# test begin


@csrf_exempt
def test(request):
    """
    @api {get} /specificApis/test test
    @apiVersion 1.0.0
    @apiDescription test
    @apiName test
    @apiGroup test
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
        datas = StudentData.objects.filter().values()
        dataIds = [datas[i]['id'] for i in range(len(datas))]
        ret = []
        s = []
        for id in dataIds:
            data = StudentData.objects.filter(id=id)
            startTime = data.values()[0]['startTime']
            endTime = data.values()[0]['endTime']
            duration, points = function.calDurationTime(startTime, endTime)
            ret.append(data.values()[0])
            data.update(duration=duration, points=points)
            s.append({'id': id, 'po': points})
            ret.append(data.values()[0])
        return retJson(error=0, result='success', ret=ret, s=s, mycls=function.MyEncoder)
    except Exception as e:
        return retJson(error=2, reason=str(e))

# test end

# login begin


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
    @apiGroup login
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
    @apiGroup login
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

# login end

# user begin


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


# user end

# student begin

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
        return retJson(error=-1, reason='have not login')
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
            return retJson(error=0, result="create student success")
        except Exception as e:
            return retJson(error=2, reason=str(e))
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
    if not function.check_Session(request):
        return retJson(error=-1, reason='have not login')
    if request.method == "GET":
        value = list(Student.objects.all().values())
        return retJson(error=0, result=value, mycls=function.MyEncoder)
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
    if not function.check_Session(request):
        return retJson(error=-1, reason='have not login')
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
    if not function.check_Session(request):
        return retJson(error=-1, reason='have not login')
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

# student end

# studentData begin


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
        return retJson(error=-1, reason='have not login')
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
    if not function.check_Session(request):
        return retJson(error=-1, reason='have not login')
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
    if not function.check_Session(request):
        return retJson(error=-1, reason='have not login')
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
                            return retJson(error=0, values=values, mycls=function.MyEncoder)
                        except Exception as e:
                            return retJson(error=7, reason=str(e))
                    else:
                        # 开始过
                        return retJson(error=6, reason='cant ask for leave')
                else:
                    return retJson(error=5, reason='not over yet')
            else:
                return retJson(error=4, reason='has asked for leave')
        else:
            return retJson(error=2, reason='Students dont exist')
    else:
        return retJson(error=1, reason='needmethod: post')


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
        return retJson(error=-1, reason='have not login')
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
                            return retJson(error=0, state=0)
                        else:
                            # 今天开始过
                            st = flag_notStart.values()[0]['startTime'].strftime(
                                '%Y-%m-%d %H:%M:%S')
                            et = flag_notStart.values()[0]['endTime'].strftime(
                                '%Y-%m-%d %H:%M:%S')
                            points = flag_notStart.values()[0]['points']
                            return retJson(error=0, state=3, starttime=st, endtime=et, points=points,  mycls=function.MyEncoder)
                    else:
                        st = flag_notOver.values()[0]['startTime'].strftime(
                            '%Y-%m-%d %H:%M:%S')
                        dataId = flag_notOver.values()[0]['id']
                        # 没结束
                        return retJson(error=0, state=2, starttime=st, dataId=dataId)
                else:
                    return retJson(error=0, state=1)  # 请假
            else:
                return retJson(error=3, reason='Students dont exist')
        except Exception as e:
            return retJson(error=2, reason=str(e))
    else:
        return retJson(error=1, reason='needmethod: post')


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
        return retJson(error=-1, reason='have not login')
    if request.method == "GET":
        try:
            username = request.session.get('username')
            classNumber = User.objects.filter(username=username).values()[
                0]['classNumber']
            stu = Student.objects.filter(
                classNumber__classNumber=classNumber).values()
            return retJson(error=0, result=list(stu), mycls=function.MyEncoder)
        except Exception as e:
            return retJson(error=2, reason=str(e))
    else:
        return retJson(error=1, reason='needmethod: get')


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
        return retJson(error=0, result=ret)
    except Exception as e:
        return retJson(error=2, reason=str(e))

# studentData end


# show begin

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
    if not function.check_Session(request):
        return retJson(error=-1, reason='have not login')
    if request.method == "POST":
        try:
            studentId = request.POST.get('studentId')
            student, stuDatas = function.getStudentData(studentId)
            return retJson(error=0, student=student, data=list(stuDatas), mycls=function.MyEncoder)
        except Exception as e:
            return retJson(error=2, reason=str(e))
    else:
        return retJson(error=1, reason='needmethod: post')


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
    if not function.check_Session(request):
        return retJson(error=-1, reason='have not login')
    if request.method == "POST":
        try:
            classNumber = request.POST.get('classNumber')
            classs, students = function.getClassData(classNumber)

            return retJson(error=0, classs=classs, data=list(students), mycls=function.MyEncoder)
        except Exception as e:
            return retJson(error=2, reason=str(e))
    else:
        return retJson(error=1, reason='needmethod: get')


@csrf_exempt
def getAllClass(request):
    """
    @api {get} /specificApis/show/getAllClass getAllClass
    @apiVersion 1.0.0
    @apiDescription get this grades's all class info
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
            return retJson(error=0, result=result, classInfo=classInfo, mycls=function.MyEncoder)
        except Exception as e:
            return retJson(error=2, reason=str(e))
    else:
        return retJson(error=1, reason='needmethod: get')


# show end


# export start
@csrf_exempt
def export(request):
    """
    @api {get} /specificApis/export export
    @apiVersion 1.0.0
    @apiDescription export student info
    @apiName export
    @apiGroup export
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
    if request.method == "GET":
        try:
            now = datetime.now().strftime('%Y_%m_%d')
            filename = '学生信息_' + now + '.xlsx'
            base_dir = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.join(
                base_dir, 'download', 'file', filename)  # 下载文件的绝对路径

            # 写入
            students = list(Student.objects.all().values())
            for stuInfo in students:
                info = function.getStudentData(stuInfo["studentId"])[0]
                stuInfo.update(info)
            ret = function.write_excel_xlsx(file_path, students)
            if ret != 'success':
                return retJson(error=3, reason=ret)

            # 输出
            file = open(file_path, 'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{}"'.format(
                filename).encode('utf-8')
            return response
        except Exception as e:
            return retJson(error=2, reason=str(e))
    else:
        return retJson(error=1, reason='needmethod: get')
# export end
