import hashlib
import json
import time
import decimal
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
    startTime = '8:30:00'
    endTime = '22:00:00'
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


def checkExist_student(studentId):
    from specificApis import models

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


# st = datetime(2020, 9, 21, 20, 0, 0, 583339)
# et = datetime(2020, 9, 21, 23, 0, 0, 583339)
# print(calDurationTime(st, et))
