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
import collections
import operator
from .models import Post
from django.views import generic
import zipfile
import shutil

from rest_framework.views import APIView
from rest_framework.response import Response

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Create your views here.
def index(request):
    return redirect('login')

def user(request):
    return request.session.get('count')
class PostList(generic.ListView,View):
    model = Post
    Post.objects.order_by('-created_on').all()
    template_name = 'counts.html'
    
@login_required(login_url='/login/')
def dashboard(request,methods=['POST', 'GET']):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        osa = request.POST['OS']
        print(osa)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print(filename)
        file1 = os.path.join(settings.MEDIA_ROOT, myfile.name)
        print(file1)
        
        if osa == "Android":
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
                
            s = [(k, dicti[k]) for k in sorted(dicti, key=dicti.get, reverse=True)]
            f_dicti={}
            #print(s)
            s = Convert(s, f_dicti)
            print("Gz",s)
            string=''
            num = ''
            for i in dicti:
                string += str(dicti[i]) + " ;;; "
                num += i + " ;;; "
            messages.info(request , string)
            print(string)
            request.session['count'] = string
            request.session['num'] = num

            user = User.objects.get(username=request.user.username)
            print(user)
            one = str(list(iter(s))[0]) + ":"+ str(s.get(list(iter(s))[0]))
            two = str(list(iter(s))[1]) + ":"+ str(s.get(list(iter(s))[1]))
            three = str(list(iter(s))[2]) + ":"+ str(s.get(list(iter(s))[2]))
            wser1 = Post(user_name = user, file_name=filename,one=one, two=two,three=three)
            wser1.save()
            file.close()
            os.remove(file1)
            final_data = {
                    "phon" : f_dicti.keys(),
                    "msgs" : f_dicti.values()
                }
            #request.session['data'] = final_data
            return render(request,"dashboard.html",final_data)
        elif osa == "iOS":
            file_extract = os.mkdir(file1+'extract')
            with zipfile.ZipFile(file1, 'r') as zip_ref:
                zip_ref.extractall(file1+'extract')
            
            file = open(file1+'extract/_chat.txt',encoding="utf8")

            
            print("Done Boyzz")
            c=0
            mem = []
            dicti={}
            #print("I reached my waypoint")
            
            while True:
                line = file.readline()
                x = re.search(r"(.*?\d.*?\,.*?].*?\:)", line)
                if x:
                    r = re.search(r"(].*?:)",x.group()).group()[2:-1]
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
                
            s = [(k, dicti[k]) for k in sorted(dicti, key=dicti.get, reverse=True)]
            f_dicti={}
            #print(s)
            s = Convert(s, f_dicti)
            print("Gz",s)
            string=''
            num = ''
            for i in dicti:
                string += str(dicti[i]) + " ;;; "
                num += i + " ;;; "
            messages.info(request , string)
            print(string)
            request.session['count'] = string
            request.session['num'] = num

            user = User.objects.get(username=request.user.username)
            print(user)
            one = str(list(iter(s))[0]) + ":"+ str(s.get(list(iter(s))[0]))
            two = str(list(iter(s))[1]) + ":"+ str(s.get(list(iter(s))[1]))
            three = str(list(iter(s))[2]) + ":"+ str(s.get(list(iter(s))[2]))
            user1 = Post(user_name = user, file_name=filename,one=one, two=two,three=three)
            print(user1.save())
            file.close()
            shutil.rmtree(file1+'extract')
            os.remove(file1)
            final_data = {
                    "phon" : f_dicti.keys(),
                    "msgs" : f_dicti.values()
                }
            #request.session['data'] = final_data
            return render(request,"dashboard.html",final_data)

    elif request.method == 'POST':
        value=request.POST['login']
        if value is not None:
            redirect('login')
    return render(request, 'dashboard.html')

def Convert(tup, di): 
    di = dict(tup) 
    return di 
      
def user_login(request):
    if request.method == "POST":

        print(settings.MEDIA_ROOT)
        username = request.POST['username']
        password =  request.POST['password']
        request.session['user'] = username

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
        email = request.POST['email']

        phone_number = request.POST['lname']
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
                user = User.objects.create_user(first_name = first_name, last_name=phone_number,username=email, password=password)
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

def chart_view(request, *args, **kwargs):
    data_string = request.session.get('data')
    data_string.split(" ;;; ")
    print(data_string)
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})

class PieView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'piecharts.html', {"customers": 10})

def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        stri = request.session.get('count')
        num = request.session.get('num')
        try:
            stri = stri.split(" ;;; ")
            num = num.split(" ;;; ")
        except AttributeError:
            pass
        print(stri)
        print(num)
        int_num = []
        for i in stri:
            try:
                print(i)
                int_num.append(int(i))
            except ValueError:
                pass
        print(num,stri)
        data = {
                "labels": num,
                "default": int_num,
        }
        return Response(data)


class PieChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        stri = request.session.get('count')
        num = request.session.get('num')
        try:
            stri = stri.split(" ;;; ")
            num = num.split(" ;;; ")
        except AttributeError:
            pass
        print(stri)
        print(num)
        int_num = []
        for i in stri:
            try:
                print(i)
                int_num.append(int(i))
            except ValueError:
                pass
        print(num,stri)
        data = {
                "labels": num,
                "default": int_num,
        }
        return Response(data)
