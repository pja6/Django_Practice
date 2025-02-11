from django.shortcuts import render

from .models import Post

def post_list(request):
    posts = Post.objects.all()  # Get all blog posts from the database
    return render(request, 'blog/post_list.html', {'posts': posts})