from django.shortcuts import render, redirect
from .models import Post



def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'Blog/posts_list.html', {'posts': posts})

def post_like(request):
    post_id = request.POST['post_id']
    post = Post.objects.get(id=post_id)
    post.likes += 1
    post.save()
    return redirect('posts_list') 
        
    

