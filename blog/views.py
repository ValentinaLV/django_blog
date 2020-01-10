from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm


def posts(request):
    posts_ = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts_})


def tags(request):
    tags_ = Tag.objects.all()
    return render(request, 'tags.html', context={'tags': tags_})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'post_details.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'post_create.html'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'post_update.html'


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'post_delete.html'
    redirect_url = 'posts_url'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'tag_details.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'tag_update.html'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'tag_delete.html'
    redirect_url = 'tags_url'
    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     return render(request, 'tag_delete.html', context={'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     tag.delete()
    #     return redirect(reverse('tags_url'))
