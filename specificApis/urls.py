from django.urls import path, include
# from specificApis import apis
from specificApis.api import ImportExport, show, studentData, student, user


urlpatterns = [
    #path('test', apis.test, name='test'),
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
