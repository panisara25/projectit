from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User, auth
from account.models import *
from account.forms import *
from .models import *
from .forms import *
from .filters import JobFilter


# Create your views here.

def index(request):
    post = PostJob.objects.all().order_by('-id')
    myFilter = JobFilter(request.GET, queryset=post)
    post = myFilter.qs

    context = {'post':post,'myFilter':myFilter}

    return render(request, "index.html", context)

def post_detail(request, pk):
    posts = PostJob.objects.get(pk=pk)
    jobs = PostJob.objects.exclude(pk=pk)
    if request.method=='POST':
        form = ApplicationForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.jobpost = posts
            instance.applicant = request.user
            instance.save()
            return redirect('/')
        else:
            return render(request, "post_detail.html", {'posts':posts,'jobs':jobs , 'form':form})
    else:
        form = ApplicationForm()      
        return render(request, "post_detail.html", {'jobs': jobs , 'posts': posts, 'form': form })


def about(request):
    return render(request, 'about.html', )

def contact(request):
    return render(request, 'contact.html')

def createPost(request):
   form = PostForm()
   if request.method == 'POST' :
 
       form = PostForm(request.POST,request.FILES)
       if form.is_valid():
           user = form.save(commit=False)
           user.user = request.user
           user.save()
           return redirect('/')


   context = {'form': form }
   
   return render(request, 'post_form.html', context)


def updatePost(request, pk):
    post = PostJob.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST' :
       #print('Create !!' , request.POST)
       form = PostForm(request.POST,request.FILES,instance=post)
       if form.is_valid():
           form.save()
           return redirect('company_profile')

    context = {'form': form }
    return render(request, 'post_form.html', context)

def deletePost(request, pk):
	post = PostJob.objects.get(id=pk)
	if request.method == "POST":
		post.delete()
		return redirect('company_profile')

	context = {'item':post}
	return render(request, 'delete.html', context)

def list_app(request,pk):
    posts = PostJob.objects.get(pk=pk)
    
    context = {
        "posts": posts,
    }
    return render(request, 'list_app.html',context)




