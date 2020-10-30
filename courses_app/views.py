from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def index(request):
    context = {
        'all_courses': Courses.objects.all(),
    }
    return render(request, "index.html", context)

def new_course(request):
    if request.method=="POST":
        errors = Courses.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
    Courses.objects.create(
        name=request.POST['name'],
        desc=request.POST['desc']
    )
    return redirect('/')

def maybe_delete(request, course_id):
    context = {
        'course': Courses.objects.get(id=course_id)
    }
    return render(request, "delete.html", context)

def delete_course(request, course_id):
    bye = Courses.objects.get(id=course_id)
    bye.delete()
    return redirect('/')