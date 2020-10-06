from django.urls import path, include
from specificApis import apis

urlpatterns = [
    path('test', apis.test, name='test'),
    path('user/add', apis.userAdd, name='userAdd'),
    path('user/changePass', apis.userChangePass, name='userChangePass'),
    path('user/getUsername', apis.getUsername, name='getUsername'),
    path('user/checkPass', apis.checkPass, name='checkPass'),

    path('login/login', apis.login, name='login'),
    path('login/logout', apis.logout, name='logout'),

    path('student/add', apis.studentAdd, name='studentAdd'),
    path('student/get', apis.studentGet, name='studentGet'),
    path('student/change', apis.studentChange, name='studentChange'),
    path('student/delete', apis.studentDelete, name='studentDelete'),

    path('studentData/signIn', apis.signIn, name='signIn'),
    path('studentData/signOut', apis.signOut, name='signOut'),
    path('studentData/askLeave', apis.askLeave, name='askLeave'),
    path('studentData/signOutCron', apis.signOutCron, name='signOutCron'),
    path('studentData/getStudentstates',
         apis.getStudentStates, name='getStudentStates'),
    path('studentData/getClassStudents',
         apis.getClassStudents, name='getClassStudents'),

    path('show/getAllClass', apis.getAllClass, name='getAllClass'),
    path('show/getClassData', apis.getClassData, name='getClassData'),
    path('show/getStudentData', apis.getStudentData, name='getStudentData'),
]
