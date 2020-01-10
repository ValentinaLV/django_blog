from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin
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
    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(instance=tag)
    #     return render(request, 'tag_update.html', context={'form': bound_form, 'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(request.POST, instance=tag)
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'tag_update.html', context={'form': bound_form, 'tag': tag})
