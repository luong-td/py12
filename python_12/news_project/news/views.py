from typing import ContextManager
from django.http import HttpResponse
from django.shortcuts import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from news.forms import CommentForm
import random

# Create your views here.

def home(request):
    categorys = Category.objects.all()
    news = New.objects.all()
    latest_post = []
    latest_post1 = []
    top_post = []
    trending = random.sample(list(news), 6)

    for i in news:
        if len(top_post) < 5:
            top_post.append(i)

    for i in range(len(news)-1, -1, -1):
        if len(latest_post) < 5:
            latest_post.append(news[i])
        if len(latest_post1) < 3:
            latest_post1.append(news[i])


    context = {
        "Trending" : trending,
        "Top_post" : top_post,
        "Latest_post" : latest_post1,
        "Latest_post_1" : latest_post[0],
        "Latest_post_2" : latest_post[1],
        "Latest_post_3" : latest_post[2],
        "Latest_post_4" : latest_post[3],
        "Latest_post_5" : latest_post[4],
        "Categorys" : categorys
    }
    return render(request, 'index.html', context)
@login_required(login_url='login')

def category(request, id):
    categorys = Category.objects.all()
    arr = New.objects.all()
    top_post , last_post = [], []
    for i in arr:
        if i.category.id == id :
            if len(top_post) < 4:
                top_post.append(i)
    for i in range(len(arr)-1, -1, -1):
        if len(last_post) < 3:
            last_post.append(arr[i])
    context = {
        "Categorys" : categorys,
        "news" : arr,
        "top_Post" : top_post,
        "last_Post" : last_post
    }
    return render(request, 'category.html', context)
@login_required(login_url='login')

def blog(request):
    categorys = Category.objects.all()
    context = {
        "Categorys" : categorys
    }
    return render(request, 'blog.html', context)
@login_required(login_url='login')
def blog_details(request):
    categorys = Category.objects.all()
    context = {
        "Categorys" : categorys
    }

    return render(request, 'blog_details.html', context)
@login_required(login_url='login')

def about(request):
    categorys = Category.objects.all()
    context = {
        "Categorys" : categorys
    }
    return render(request, 'about.html', context)
@login_required(login_url='login')

def contact(request):
    categorys = Category.objects.all()
    context = {
        "Categorys" : categorys
    }
    return render(request, 'contact.html', context)
@login_required(login_url='login')

def elements(request):
    categorys = Category.objects.all()
    context = {
        "Categorys" : categorys
    }
    return render(request, 'elements.html', context)
@login_required(login_url='login')
 
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'login.html', context)
def logoutUser(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def sign_up(request):
    form = UserCreationForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Account was created')
                return redirect('login')     
        context = {'form':form}
        return render(request, 'sin-up.html', context)
@login_required(login_url='login')

def my_Main(request):
    categorys = Category.objects.all()
    context = {
        "Categorys" : categorys
    }
    return render(request, 'main.html', context)
@login_required(login_url='login')

def post_details(request, id):
    categorys = Category.objects.all()
    new = New.objects.get(pk=id)
    context = {
        "Categorys" : categorys,
        "new" : new
    }
    
    return render(request, 'post_details.html', context)
@login_required(login_url='login')

def feedback(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        Feedback.objects.create(message=message, name=name, email=email, subject=subject)
        return HttpResponse("<h1>Success</h1>")
    return redirect('/contact')
@login_required(login_url='login')

def search(request):

    news = New.objects.all()
    last_post = []
        
    for i in range(len(news)-1, -1, -1):
        if len(last_post) < 3:
            last_post.append(news[i])

    print(request.method)
    if request.method == 'GET':
        try:
            search = request.GET['search'].lower().split()
        except:
            return redirect('/')

        res  = []
        for new in news:
            for text in search:
                if text in new.title.lower():
                    res.append(new)
                    break
        return render(request,'search.html', {'news':res, 'search':request.GET['search'], 'last_Post' : last_post})
    return redirect('/', {'last_Post' : last_post})

