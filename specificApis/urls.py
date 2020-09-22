from django.urls import path, include
from specificApis import apis

urlpatterns = [
    path('test', apis.test, name='test'),
    path('user/add', apis.userAdd, name='userAdd'),
    path('user/changePass', apis.userChangePass, name='userChangePass'),

    path('student/add', apis.studentAdd, name='studentAdd'),
    path('student/get', apis.studentGet, name='studentGet'),
    path('student/change', apis.studentChange, name='studentChange'),
    path('student/delete', apis.studentDelete, name='studentDelete'),

    path('studentData/signIn', apis.signIn, name='signIn'),
    path('studentData/signOut', apis.signOut, name='signOut'),
    path('studentData/askLeave', apis.askLeave, name='askLeave'),
]
