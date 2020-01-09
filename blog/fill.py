from blog.models import Post
from blog.models import Tag

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

p_1 = Post.objects.get(slug='new-slug')
p_1.slug = 'new-post'
p_1.save()
p_2 = Post.objects.get(slug='new-slug2')
p_2.slug = 'new-post2'
p_2.save()
p_3 = Post.objects.get(slug='new-slug3')
p_3.slug = 'new-post3'
p_3.save()
p_4 = Post.objects.get(slug='new-slug4')
p_4.slug = 'new-post4'
p_4.save()
p_5 = Post.objects.get(slug='new-slug5')
p_5.slug = 'new-post5'
p_5.save()
p_6 = Post.objects.get(slug='new-slug6')
p_6.slug = 'new-post6'
p_6.save()

t1 = Tag.objects.create(title='python', slug='python')
p_1.tags.add(t1)
t2 = Tag.objects.create(title='django', slug='django')
t3 = Tag.objects.create(title='flask', slug='flask')
t4 = Tag.objects.create(title='skills', slug='skills')
t5 = Tag.objects.create(title='development', slug='development')
p_1.tags.add(t2)
p_1.tags.add(t3)
p_1.tags.add(t4)
p_1.tags.add(t5)
