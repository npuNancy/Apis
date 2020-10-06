import hashlib
import json
import time
import decimal
from specificApis import models
from datetime import datetime, timedelta, timezone, date


class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            return json.JSONEncoder.default(self, obj)


class config():
    startTime = '18:30:00'
    endTime = '22:30:00'
    atMostTime = 3.0  # hours
    pointsPerHour = 1.0  # 1.0 point per hour
    requiredPoints = 120.0


def hash(password):
    salt = '@'
    md5 = hashlib.md5()
    md5.update((password+salt).encode('utf-8'))
    return md5.hexdigest()


def UTC0_2_UTC8(utc0Time):
    # 数据库UTC时间 改成 UTC+8
    utc8Time = utc0Time.astimezone(timezone(timedelta(hours=8)))
    utc8Time = utc8Time.replace(tzinfo=None)

    return utc8Time


def check_Session(request):
    username = request.session.get('username')
    return True if username else False


def checkExist_student(studentId):
    flag = models.Student.objects.filter(studentId=studentId)
    return True if flag else False


def calDurationTime(startTime, endTime):
    confi = config()
    latestTime = datetime.strptime(confi.endTime, '%H:%M:%S')
    endTime_ = datetime.strptime(
        endTime.strftime('%H:%M:%S'), '%H:%M:%S')
    if endTime_ > latestTime:
        d = (endTime_ - latestTime).seconds
    else:
        d = 0

    duration = (endTime - startTime).seconds - d
    mostSeconds = confi.atMostTime * 60 * 60
    if duration > mostSeconds:
        duration = mostSeconds
    points = (duration / 3600) * confi.pointsPerHour
    points = round(points, 1)
    return duration, points


def check_UserPass(username, password):
    user_obj = models.User.objects.filter(username=username, password=password)
    ret = True if user_obj else False
    return ret


def getStudentData(studentId):
    student = models.Student.objects.filter(studentId=studentId).values()[0]
    points = student['initPoints']  # 总积分
    stuDatas = models.StudentData.objects.filter(
        studentId__studentId=studentId).values()

    durations = 0  # 总时长s
    for data in stuDatas:
        points += int(data['points'])
        durations += int(data['duration'])
    student['number'] = len(stuDatas)  # 总次数
    student['durations'] = durations
    student['averTime'] = durations / len(stuDatas) if len(stuDatas) else 0
    student['points'] = points

    return student, stuDatas


def getClassData(classNumber):
    c = config()
    requiredPoints = c.requiredPoints

    students = models.Student.objects.filter(
        classNumber__classNumber=classNumber).values()
    points = 0
    durations = 0
    requiredPeople = 0
    stuDatas = []
    for stud in students:
        stuId = stud['studentId']
        stuInfo = getStudentData(stuId)[0]
        if stud['state'] == 0:  # 除去免自习的人
            points += stuInfo['points']
            durations += stuInfo['averTime']
            requiredPeople += 1 if points >= requiredPoints else 0
        stuDatas.append(stuInfo)

    classs = {
        'classNumber': classNumber,
        'number': len(students),  # 人数
        'points': points,
        'requiredPeople': requiredPeople,
        'averDurations': durations / len(students) if len(students) else 0
    }

    return classs, stuDatas


def cron_signOut():
    try:
        datas = models.StudentData.objects.filter(state=2).values()
        dataIds = [datas[i]['id'] for i in range(len(datas))]
        for id in dataIds:
            data = models.StudentData.objects.get(id=id)
            data.state = 3
            data.save()
            data = models.StudentData.objects.filter(id=id).values()[0]
            startTime = data['startTime']
            endTime = data['endTime']
            duration, points = calDurationTime(startTime, endTime)
            data.update(duration=duration, points=points)
        return 'success'
    except Exception as e:
        return str(e)
