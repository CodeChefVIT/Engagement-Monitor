from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    return HttpResponse('<h1>Madu</h1>')

def uploader(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'form.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'form.html')

def login(request):
    if request.method == "POST":
        phone = request.POST['number']
        password =  request.POST['password']
        print(password)
        user = auth.authenticate(username=phone,password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            print("LOGIN SUCCESS")
            redirect('/')
        else:
            messages.info(request, "Wrong Credentials")
            return redirect('login')
        return redirect('/up')
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
                return redirect('login')
            elif User.objects.filter(username = phone_number).exists():
                messages.info(request , "Phone NUmber Already Exisits")
                return redirect('login')
            else:
                user = User.objects.create_user(first_name = first_name, last_name=last_name,username=phone_number, email=email,password=password)
                user.save()
                redirect('login')
        else:
            messages.info(request, "Password Not Matching")
            redirect('register')
        return redirect('login/')
    else:
        return render(request , 'register.html')
    
def logout(request):
    pass