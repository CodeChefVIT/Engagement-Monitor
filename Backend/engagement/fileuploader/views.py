from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import os
import re
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.generic import View
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Create your views here.
def index(request):
    return render(request,"ajax_trial.html")

@login_required(login_url='/login/')
def dashboard(request,methods=['POST', 'GET']):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print(filename)
        file1 = os.path.join(settings.MEDIA_ROOT, myfile.name)
        print(file1)
        file = open(file1,encoding="utf8")
        c=0
        mem = []
        dicti={}
        #print("I reached my waypoint")
        while True:
            line = file.readline()
            x = re.search(r"(\d.*?\,.*?-.*?\:)", line)
            if x:
                r = re.search(r"(-.*?:)",x.group()).group()[2:-1]
                c+=1

                if (r in mem): 
                    #print ("Member Exists") 
                    for i in dicti:
                        if(i==r):
                            a = dicti[i]
                            up = {r:a+1}
                            dicti.update(up)
                            #print(up)
                else:
                    mem.append(r)
                    up = {r:1}
                    dicti.update(up)
            if not line:
                z=0
                break
        for i in dicti :  
            z+=dicti[i]
        print(dicti)
        print(z,c)
        messages.info(request , dicti)
        file.close()
        os.remove(file1)
        final_data = {
                "phon" : dicti.keys(),
                "msgs" : dicti.values()
            }
        return render(request,"dashboard.html",final_data)
    elif request.method == 'POST':
        value=request.POST['login']
        if value is not None:
            redirect('login')
    return render(request, 'dashboard.html')

@login_required(login_url='/login/')
def uploader(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print(filename)
        file1 = os.path.join(settings.MEDIA_ROOT, myfile.name)
        print(file1)
        file = open(file1,encoding="utf8")
        c=0
        mem = []
        dicti={}
        #print("I reached my waypoint")
        while True:
            line = file.readline()
            x = re.search(r"(\d.*?\,.*?-.*?\:)", line)
            if x:
                r = re.search(r"(-.*?:)",x.group()).group()[2:-1]
                c+=1

                if (r in mem): 
                    #print ("Member Exists") 
                    for i in dicti:
                        if(i==r):
                            a = dicti[i]
                            up = {r:a+1}
                            dicti.update(up)
                            #print(up)
                else:
                    mem.append(r)
                    up = {r:1}
                    dicti.update(up)
            if not line:
                z=0
                break
        for i in dicti :  
            z+=dicti[i]
        print(dicti)
        print(z,c)
        messages.info(request , dicti)
        file.close()
        os.remove(file1)
        data = {
        "sales": dicti.keys(),
        "customers": dicti.values(),
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        value=request.POST['login']
        if value is not None:
            redirect('login')
    return render(request, 'form.html')
        
def user_login(request):
    if request.method == "POST":

        print(settings.MEDIA_ROOT)
        username = request.POST['username']
        password =  request.POST['password']
        print(password)
        user = auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            print("LOGIN SUCCESS")
            redirect('/')
        else:
            messages.info(request, "Wrong Credentials")
            return redirect('login')
        return redirect('/dash')
    else:
        return render(request, 'login.html')



def register(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        phone_number = request.POST['number']
        password =  request.POST['password']
        confirm_password =  request.POST['cpassword']
        
        if password == confirm_password:
            if User.objects.filter(email = email).exists():
                messages.info(request , "Email Already exist")
                return redirect('/login')
            elif User.objects.filter(username = phone_number).exists():
                messages.info(request , "Phone NUmber Already Exisits")
                return redirect('/login')
            else:
                user = User.objects.create_user(first_name = first_name, last_name=last_name,username=email, phonenumber=phone_number,password=password)
                user.save()
                redirect('/login')
        else:
            messages.info(request, "Password Not Matching")
            redirect('register')
        return redirect('/login')
    else:
        return render(request , 'register.html')

def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login')
