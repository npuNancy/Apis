## 自习管理系统

1. 安装django
2. pip install xlwt
   pip install openpyxl
3. 在mysql执行`create database selfstudysystem`创建数据库
4. 在Apis/settings.py 配置数据库
5. 在根目录命令行执行
    `python manage.py makemigration`
    `python manage.py migrate`
    `python manage.py runserver`
6. 在浏览器访问 127.0.0.1:8000

TODO:
    把 gradeAdmin 单独拿出来
    login页面判断是否已经登录
    添加年级管理员功能