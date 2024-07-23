from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Like
from django.contrib.auth.decorators import login_required

@login_required
def add_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if not Like.objects.filter(post=post, user=request.user).exists():
        Like.objects.create(post=post, user=request.user)
    return redirect('post_detail', post_id=post_id)

@login_required
def remove_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(post=post, user=request.user).first()
    if like:
        like.delete()
    return redirect('post_detail', post_id=post_id)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    posts = Post.objects.all()
    return render(request, 'blog/post_detail.html', {'post': post, 'posts': posts})


