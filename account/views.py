from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import *
from jobboard.models import *

# Create your views here.

def login(request):
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')
            return redirect('login')

    
     else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'ชื่อผู้ใช้ถูกใช้แล้ว')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
               messages.info(request,'อีเมลนี้ถูกใช้แล้ว')
               return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'รหัสผ่านไม่เหมือนกัน')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def companyProfile(request):
    post = PostJob.objects.all().order_by('-id')
    

    context = {'post':post}
    return render(request, 'com_profile.html',context)

def editcompany(request,id):
    company = get_object_or_404(CompanyProfile,user=id)  
    if request.method == 'POST':
            company.company_name = request.POST['company_name']
            company.company_detail = request.POST['company_detail']
            company.company_address = request.POST['company_address']
            company.com_img = request.FILES.get('img',company.com_img)
            company.benifit = request.POST['benifit']
            company.contact = request.POST['contact']
            company.prove = request.FILES.get('prove',company.prove)
            company.save()
    return redirect('company_profile')



def profile(request):
    post = PostJob.objects.all().order_by('-id')
    

    context = {'post':post}
    return render(request, 'profile.html',context)

def editprofile(request,id):
    user = get_object_or_404(User,id=id)
    profile = get_object_or_404(Profile,user=id)
    print(user.id)
    print(user.username)  
    if request.method == 'POST':
            user.username = request.POST['username']
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            profile.image = request.FILES.get('img',profile.image)
            profile.resume = request.FILES.get('resume',profile.resume)
            profile.about = request.POST['about']
            user.save()
            profile.save()
    return redirect('profile')

  

