from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse
from django.db.models import Q

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