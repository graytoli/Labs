from django.shortcuts import render, get_object_or_404, redirect

from posts.models import Post, Comment

def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})

def retrieve(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/retrieve.html', {'post': post})

def create_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        comment = Comment()
        comment.body = request.POST['body']
        comment.post = post
        comment.save()
    
    return redirect('posts:retrieve', id=post.id)