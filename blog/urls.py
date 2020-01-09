from django.urls import path
from blog.views import all_posts, post_details


urlpatterns = [
    path('', all_posts, name='all_posts_url'),
    path('post/<str:slug>', post_details, name='post_details_url')
]
