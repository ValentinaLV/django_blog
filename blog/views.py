from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin
from .forms import TagForm, PostForm


def posts(request):
    posts_ = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts_})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'post_details.html'


def tags(request):
    tags_ = Tag.objects.all()
    return render(request, 'tags.html', context={'tags': tags_})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'tag_details.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'tag_create.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'post_create.html'
