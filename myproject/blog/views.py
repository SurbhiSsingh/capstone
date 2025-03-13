from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

def blog_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/blog_list.html", {"posts": posts})



def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, "blog/blog_details.html", {"post": post})

