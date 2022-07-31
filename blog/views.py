from django.shortcuts import render
from blog.models import Course, Teacher, Application
from blog.forms import ApplicationForm

# Create your views here.

def home(request):
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    context ={
        'courses':courses,
        'teachers':teachers,
    }
    return render(request,'home.html',context)

def about_detail(request,pk):
    course = Course.objects.get(pk=pk)
    context ={
        'course':course,
    }
    
    return render(request,'about_detail.html',context)

def about_course(request):
    form = ApplicationForm(request.POST or None)
    is_success = False
    if request.method == 'POST' and form.is_valid():
        is_success = True
        form.save()
        form = ApplicationForm()
    context = {
        'form': form,
        'is_success': is_success,
    }
    return render(request,'about_course.html',context)