from django.urls import path
from blog.views import post_home, post_list


urlpatterns = [
    path('', post_home),
    path('all-posts/', post_list)
]
