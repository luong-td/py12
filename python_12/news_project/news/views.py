from django.http import HttpResponse
from django.shortcuts import *
from .models import *
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

def blog(request):
    categorys = Category.objects.all()
    context = {
        "Categorys" : categorys
    }
    return render(request, 'blog.html', context)

def blog_details(request):
    categorys = Category.objects.all()
    context = {
        "Categorys" : categorys
    }
    return render(request, 'blog_details.html', context)

def about(request):
    categorys = Category.objects.all()
    context = {
        "Categorys" : categorys
    }
    return render(request, 'about.html', context)

def contact(request):
    categorys = Category.objects.all()
    context = {
        "Categorys" : categorys
    }
    return render(request, 'contact.html', context)

def elements(request):
    categorys = Category.objects.all()
    context = {
        "Categorys" : categorys
    }
    return render(request, 'elements.html', context)

def login(request):
    categorys = Category.objects.all()
    context = {
        "Categorys" : categorys
    }
    return render(request, 'login.html', context)

def sign_up(request):
    categorys = Category.objects.all()
    context = {
        "Categorys" : categorys
    }
    return render(request, 'sin-up.html', context)

def my_Main(request):
    categorys = Category.objects.all()
    context = {
        "Categorys" : categorys
    }
    return render(request, 'main.html', context)

def post_details(request, id):
    categorys = Category.objects.all()
    new = New.objects.get(pk=id)
    context = {
        "Categorys" : categorys,
        "new" : new
    }
    return render(request, 'post_details.html', context)

def feedback(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        Feedback.objects.create(message=message, name=name, email=email, subject=subject)
        return HttpResponse("<h1>Success</h1>")
    return redirect('/contact')

def search(request):
    print(request.method)
    if request.method == 'GET':
        try:
            search = request.GET['search'].lower().split()
        except:
            return redirect('/')
            
        news = New.objects.all()
        res  = []
        for new in news:
            for text in search:
                if text in new.title.lower():
                    res.append(new)
                    break
        return render(request,'search.html', {'news':res, 'search':request.GET['search']})
    return redirect('/')
