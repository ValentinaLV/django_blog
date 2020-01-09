from django.shortcuts import render
from .models import Post


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts})


def post_details(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'post_details.html', context={'post': post})
