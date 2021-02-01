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


**TODO**:
    - 年级管理员能查看所有的
    - 班级管理员只能查看自己的
    - fix：修改学生信息的bug
    - add: 修改学生积分会有相应记录


**系统管理员功能**：
   
    - 年级
        * 查看、删除（外键拒绝删除）、添加年级
    - 年级管理员
        * 查看年级管理员
        * 删除年级管理员
        * 添加年级管理员（有年级时才能添加）
**年级管理员功能**：
   
    - 数据导入导出
    - 班级
        * 查看班级
        * 删除班级：班级有同学的时候，拒绝删除
        * 添加班级：添加班级的时候同步创建一个班级管理员（密码和班号相同）
    - 班级管理员
        * 查看班级管理员
        * ~~添加班级管理员~~
        * ~~删除班级管理员（不能删除和班级绑定的那个管理员）~~
    - 查看全年级所有人的数据
**班级管理员**：
    - 只能查看本班级的
    - fix：修改学生信息的bug
    - add: 修改学生积分会有相应记录
    
    
    
