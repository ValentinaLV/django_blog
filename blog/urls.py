from django.urls import path
from blog.views import posts, post_details
from blog.views import tags, tag_details


urlpatterns = [
    path('', posts, name='posts_url'),
    path('post/<str:slug>', post_details, name='post_details_url'),
    path('tags', tags, name='tags_url'),
    path('tag/<str:slug>', tag_details, name='tag_details_url')
]
