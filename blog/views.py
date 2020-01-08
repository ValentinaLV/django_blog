from django.shortcuts import render


def post_home(request):
    return render(request, 'base_blog.html')


def post_list(request):
    n = ['Oleg', 'Inna', 'Olga']
    return render(request, 'index.html', context={'names': n})

