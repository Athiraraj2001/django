from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from .forms import User1Form
from .models import User1

# Create your views here.
def Home(request):
    return render(request,'home.html')

def signup(request):
    if request.method=='POST':
        Fullname=request.POST['Full Name']
        email=request.POST['email']
        password=request.POST['password']
        myuser=User.objects.create_user(Fullname,email,password)
        myuser.save()
        return redirect('/signin')
    return render(request,'sign up.html')

def signin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            return render(request,'about.html')
        else:
            return redirect('/about')
    return render(request, 'sign in.html')

def Logout(request):
    logout(request)
    return render(request,'home.html')

def add(request):
    if request.method=='POST':
        fm=User1Form(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=User1Form()
    per=User1.objects.all()
    return render(request,'about.html',{'form':fm,'sp':per})

def delete(request,id):
    if request.method=='POST':
        per1=User1.objects.get(pk=id)
        per1.delete()
        return redirect('/about')

def edit(request,id):
    if request.method=='POST':
        per2=User1.objects.get(pk=id)
        fm=User1Form(request.POST,instance=per2)
        if fm.is_valid():
            fm.save()
        else:
            per2=User1.objects.get(pk=id)
            fm=User1Form(instance=per2)
    return render(request,'edit.html',{'form':fm})