from django.urls import path, include
# from specificApis import apis
from specificApis.api import ImportExport, show, studentData, student, user, admin, grade


urlpatterns = [
    #path('test', apis.test, name='test'),

    path('admin/add', admin.adminAdd, name='adminAdd'),
    path('admin/login', admin.login, name="adminLogin"),
    path('admin/logout', admin.logout, name="adminLogout"),
    path('admin/checkPass', admin.checkPass, name='checkPass'),
    path('admin/changePass', admin.changePass, name='changePass'),

    path('admin/gradeAdminAdd', admin.gradeAdminAdd, name='gradeAdminAdd'),
    path('admin/gradeAdminGetAll', admin.gradeAdminGetAll, name='gradeAdminGetAll'),
    path('admin/gradeAdminDelete', admin.gradeAdminDelete, name='gradeAdminDelete'),
    path('admin/gradeAdminLogout', admin.gradeAdminLogout, name='gardeAdminLogout'),

    path('grade/gradeAdd', grade.gradeAdd, name='gradeAdd'),
    path('grade/gradeGetAll', grade.gradeGetAll, name='gradeGetAll'),
    path('grade/gradeDelete', grade.gradeDelete, name='gradeDelete'),

    path('user/add', user.userAdd, name='userAdd'),
    path('user/changePass', user.userChangePass, name='userChangePass'),
    path('user/getUsername', user.getUsername, name='getUsername'),
    path('user/checkPass', user.checkPass, name='checkPass'),
    path('user/getUserClassNumber',
         user.getUserClassNumber, name='getUserClassNumber'),

    path('login/login', user.login, name='login'),
    path('login/logout', user.logout, name='logout'),

    path('student/add', student.studentAdd, name='studentAdd'),
    path('student/get', student.studentGet, name='studentGet'),
    path('student/change', student.studentChange, name='studentChange'),
    path('student/delete', student.studentDelete, name='studentDelete'),

    path('studentData/signIn', studentData.signIn, name='signIn'),
    path('studentData/signOut', studentData.signOut, name='signOut'),
    path('studentData/askLeave', studentData.askLeave, name='askLeave'),
    path('studentData/signOutCron', studentData.signOutCron, name='signOutCron'),
    path('studentData/getStudentstates',
         studentData.getStudentStates, name='getStudentStates'),
    path('studentData/getClassStudents',
         studentData.getClassStudents, name='getClassStudents'),

    path('show/getAllClass', show.getAllClass, name='getAllClass'),
    path('show/getClassData', show.getClassData, name='getClassData'),
    path('show/getStudentData', show.getStudentData, name='getStudentData'),

    path('export', ImportExport.export, name='export'),

]
