from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse
from django.db.models import Q
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Create your views here.
def home(request):
    featured_posts = Blog.objects.filter(is_featured=True).order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    print(featured_posts)
    context = {'featured_posts': featured_posts, 'posts': posts}
    return render(request, 'home.html', context)


def category(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    category = Category.objects.get(pk=category_id)
    context = {'posts': posts, 'category': category}
    return render(request, 'category.html', context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {'single_blog': single_blog}
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter( 
        Q(title__icontains=keyword) | 
        Q(short_description__icontains=keyword) | 
        Q(blog_body__icontains=keyword)
        )
    context = {'blogs': blogs, 'keyword': keyword}
    return render(request, 'search.html', context)


#login, registrations functionality
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')    
    form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')