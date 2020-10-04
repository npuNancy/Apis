from django.urls import path, include
from SelfStudySystem import views

urlpatterns = [
    path('', views.signIn, name='signIN'),
    path('signIn', views.signIn, name='signIN'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('changePass', views.changePass, name='changePass'),
    path('class', views.classes, name='classes'),
    path('student', views.student, name='student'),
]
