from blog.models import Post

# ./manage.py shell

p = Post(title='New Post', slug='new-slug', body='new post body')
p.save()
# w/o save()
p1 = Post.objects.create(title='New Post2', slug='new-slug2', body='new post body2')

Post.objects.all()
post = Post.objects.get(slug='New-slug2')
post2 = Post.objects.get(slug__iexact='New-slug2')  # <Post: New Post2>
post3 = Post.objects.filter(slug__contains='new')  # <QuerySet [<Post: New Post>, <Post: New Post2>]>

p2 = Post.objects.create(title='New Post3', slug='new-slug3', body='new post body3')
p3 = Post.objects.create(title='New Post4', slug='new-slug4', body='new post body4')
p4 = Post.objects.create(title='New Post5', slug='new-slug5', body='new post body5')
p5 = Post.objects.create(title='New Post6', slug='new-slug6', body='new post body6')
