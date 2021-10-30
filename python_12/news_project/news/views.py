from django.shortcuts import render
from .models import Category, New

# Create your views here.

def home(request):
    categorys = Category.objects.all()
    context = {
        "Categorys" : categorys
    }
    return render(request, 'index.html', context)

def category(request, id):
    categorys = Category.objects.all()
    arr = New.objects.all()
    top_post , last_post = [], []
    for i in arr:
        if i.category.id == id :
            if len(top_post) < 5:
                top_post.append(i)
            else: last_post.append(i)
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
