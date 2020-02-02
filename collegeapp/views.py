from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import College

# Create your views here.
def index(request):
    return render(request,'index.html')
def submit(request):
    if request.method == 'POST':
        department = request.POST['department']
        name = request.POST['name']
        roll_no = request.POST['roll_no']
        section = request.POST['section']
        game = request.POST['game']
        
        college = College(department=department,name=name,roll_no=roll_no,section=section,game=game)
        #user =User.objects.create_user(first_name=first_name,last_name=last_name,username=username)

        college.save();
        messages.info(request,'Succefully submited')
        return redirect('index.html')
    else:
        return render(request,'submit.html')