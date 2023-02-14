from email import message
from urllib import request
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from accounts.models import contactEnquiry
from .models import contactEnquiry
from django.shortcuts import render


# Create your views here.
from .forms import RegisterForm








from django import forms
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget,AdminSplitDateTime






def index(request):
    return render(request,'accounts/index.html',{})


def registerUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'accounts/register.html',{'form':form})

def loginUser(request):
    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']

        if username and password:
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'username or password is incorrect')
        else:
            messages.error(request,'fill out all the fields')

    return render(request,'accounts/login.html',{})

def home(request):
    return render (request,'accounts/home.html',{})

def logoutUser(request):
    logout(request)
    return redirect('index')

def service(request):
    return render (request,'accounts/service.html',{})

def portfolio(request):
    return render (request,'accounts/portfolio.html',{})

def clients(request):
    return render(request,'accounts/clients.html',{})

def about(request):
    return render(request,'accounts/about.html',{})

def contact(request):
    return render(request,'accounts/contact.html',{})

def arial(request):
    return render(request,'accounts/arial.html',{})

def video(request):
    return render(request,'accounts/video.html',{})

def mapping(request):
    return render(request,'accounts/3d_mapping.html',{})


def saveEnquiry(request):
    n=''
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        message = request.POST['message']

        data = contactEnquiry(name=name,email=email,subject=text,message=message)
        data.save()
        n='Message Sent Succesfully'

    return render(request,'accounts/contact.html',{'msg':n})









from .models import DTModel


class DTModelForm(forms.ModelForm):

    class Meta:
        model =DTModel
        fields ="__all__"




class DTForm(forms.Form):
    your_name = forms.CharField(max_length=64)
    date_input = forms.DateField(widget=AdminDateWidget())
    time_input = forms.DateField(widget=AdminTimeWidget())
    date_time_input = forms.DateField(widget=AdminSplitDateTime())

def index1(request):
    form = DTForm()
    return render(request,'accounts/calender.html',{'form':form})


def index_v2(request):
    form = DTModelForm()
    return render(request,'accounts/calender_1.html',{'form':form})
