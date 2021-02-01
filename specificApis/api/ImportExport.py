import json
import os
from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db import transaction
from specificApis.models import *
from specificApis import function


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
            filename = 'student_info_' + now + '.xlsx'
            base_dir = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.join(
                base_dir, 'file', 'download',  filename)  # 下载文件的绝对路径

            # 写入
            students = list(Student.objects.all().values())
            for stuInfo in students:
                info = function.getStudentData(stuInfo["studentId"])[0]
                stuInfo.update(info)
            ret = function.write_excel_xlsx(file_path, students)
            if ret != 'success':
                return function.retJson(error=3, reason=ret)

            # 输出
            file = open(file_path, 'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{}"'.format(
                filename).encode('utf-8')
            return response
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=1, reason='needmethod: get')


@csrf_exempt
def uploadStudentInfo(request):
    """
    @api {get} /specificApis/uploadStudentInfo uploadStudentInfo
    @apiVersion 1.0.0
    @apiDescription upload student info & write student infos
    @apiName uploadStudentInfo
    @apiGroup export
    @apiParam {file} file file
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
    if not function.check_gradeAdminSession(request):
        return function.retJson(error=-1, reason='have not login')
    if request.method == "POST":
        try:
            studentInfoFile = request.FILES.get("studentInfo", None)
            if not studentInfoFile:
                return function.retJson(error=-2, reason="no files for upload!")
            if not str(studentInfoFile.name).split('.')[-1] == 'xlsx':
                return function.retJson(error=-3, reason="need file with .xlsx")

            # 保存文件
            now = datetime.now().strftime('%Y_%m_%d')
            filename = 'student_info_' + now + '_' + studentInfoFile.name
            base_dir = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.join(
                base_dir, 'file', 'upload',  filename)  # 下载文件的绝对路径

            with open(file_path, 'wb') as f:
                for chunk in studentInfoFile.chunks():  # 分块写入文件
                    f.write(chunk)

            # 读取文件
            studentInfo = function.read_excel_xlsx(file_path)

            # 检查studentId 是否重复
            studentIdList1 = [x['studentId'] for x in studentInfo]
            studentIdList2 = set(studentIdList1)
            if len(studentIdList1) != len(studentIdList2):
                return function.retJson(error=-4, reason='stdudent id repeat')

            # 检查class 是否已存在
            classTmp = list(Classes.objects.filter().values())
            classList1 = list(set([x['class'] for x in studentInfo]))
            classList2 = [x['classNumber_id'] for x in classTmp]
            if set(classList1) <= set(classList2):
                return function.retJson(error=-5, reason='need create class first')

            # 原子操作
            with transaction.atomic():
                for std in studentInfo:
                    name = std['name']
                    state = std['state']
                    studentId = std['studentId']
                    initPoints = std['initPoints']
                    classNumber = std['class']
                    class_Account = Classes.objects.get(
                        classNumber=classNumber)
                    student_Account__ = Student(classNumber=class_Account, sex=0,
                                                studentId=studentId, name=name,
                                                state=state, initPoints=initPoints)
                    student_Account__.save()

            return function.retJson(error=0, result="upload file success")
        except Exception as e:
            return function.retJson(error=2, reason=str(e))
    else:
        return function.retJson(error=1, reason='need method: post')
