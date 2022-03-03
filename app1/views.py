from unicodedata import name
from django.shortcuts import render
from . models import Student,Teacher

# Create your views here.
def index(request):
    if request.method=='POST':
        std_name = request.POST["uname"]
        std_age = request.POST["uage"]
        std_mark = request.POST["umark"]
        std1 = Student(name=std_name,age=std_age,mark=std_mark)
        std1.save()


    return render(request,'index.html')

def teacher(request):
    if request.method == 'POST':
        t_name = request.POST["tname"]
        t_age = request.POST["tage"]
        teacher1 = Teacher(name=t_name,age=t_age)
        teacher1.save()
        msg = "teacher added successfully"
        return render(request,'teacher.html',{'msg':msg,})
    

    return render(request,'teacher.html')

def view_teacher(request):
    teachers = Teacher.objects.all()
    return render(request,'viewteachers.html',{'details':teachers,})