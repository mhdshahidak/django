from unicodedata import name
from django import views
from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('',views.index,name='index'),
    path('teacher',views.teacher,name='teach'),
    path('viewteachers',views.view_teacher,name='viewteacher'),
]
