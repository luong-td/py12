from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'index.html', context)

def category(request):
    context = {}
    return render(request, 'category.html', context)

def blog(request):
    context = {}
    return render(request, 'blog.html', context)

def blog_details(request):
    context = {}
    return render(request, 'blog_details.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def elements(request):
    context = {}
    return render(request, 'elements.html', context)

def login(request):
    context = {}
    return render(request, 'login.html', context)

def sign_up(request):
    context = {}
    return render(request, 'sin-up.html', context)

def my_Main(request):
    context = {}
    return render(request, 'main.html', context)

def post_details(request):
    context = {}
    return render(request, 'post_details.html', context)