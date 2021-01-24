import json
import os
from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.http import HttpResponse, FileResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
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
                base_dir, 'download', 'file', filename)  # 下载文件的绝对路径

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
