from django.urls import path
from blog.views import posts, PostDetail, TagCreate
from blog.views import tags, TagDetail


urlpatterns = [
    path('', posts, name='posts_url'),
    path('post/<str:slug>', PostDetail.as_view(), name='post_details_url'),
    path('tag-s', tags, name='tags_url'),
    path('tag/create', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>', TagDetail.as_view(), name='tag_details_url')
]
