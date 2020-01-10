from django.urls import path
from blog.views import posts, PostDetail, PostCreate, PostUpdate
from blog.views import tags, TagDetail, TagCreate, TagUpdate


urlpatterns = [
    path('', posts, name='posts_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_details_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('tag-s/', tags, name='tags_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_details_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
]
