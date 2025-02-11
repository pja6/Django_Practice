from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #add in blogs
    path('', include('blog.urls')),
]