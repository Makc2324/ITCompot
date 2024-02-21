from django.shortcuts import render
from .models import Post



def posts_list(xxx):
    posts = Post.objects.all()
    return render(xxx, 'Blog/posts_list.html', {'posts': posts})
