from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Profile
from .forms import Login_form
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
# Create your views here.


def doctors_list(request):
    if request.method == 'POST' :
        print('DATE : ',request.POST)
        selected_special = request.POST['ccc']
    else :
        selected_special = False
    doctor = User.objects.all()
    return render(request,'user/doctors_list.html',{'doctors':doctor,'specializing':selected_special})

def doctors_detail(request,slug):
    doctors_details = Profile.objects.get(slug = slug)
    return render(request,'user/doctors_detail.html',{'doctors_detail':doctors_details})

def doctor_login(request):
    if request.method == 'POST':
        form = Login_form()
        userName = request.POST['username']
        password = request.POST['password']
        selected_special = request.POST['ccc']
        user = authenticate(request , username = userName , password = password)
        if user is not None :
            login(request,user)
            return redirect('accounts:doctors_list')
    else : 
        form = Login_form()
        selected_special = False
    return render(request,'user/login.html',{'form':form ,'specializing':selected_special })


@login_required()
def doc_Porfile(request):
    return render(request,'user/myProfile.html',{})