from django.shortcuts import render
from .models import *
from django.http import HttpResponse

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