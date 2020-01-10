from django.shortcuts import render, redirect
from django.views.generic import View
from django.shortcuts import get_object_or_404
from .models import Post, Tag
from .utils import ObjectDetailMixin
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


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'tag_create.html', context={'form': bound_form})


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'post_create.html', context={'form': form})




