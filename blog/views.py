from django.shortcuts import render
from .models import Post, Tag


def posts(request):
    posts_ = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts_})


def post_details(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'post_details.html', context={'post': post})


def tags(request):
    tags_ = Tag.objects.all()
    return render(request, 'tags.html', context={'tags': tags_})


def tag_details(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'tag_details.html', context={'tag': tag})
