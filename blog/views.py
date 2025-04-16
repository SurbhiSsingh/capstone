from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .models import Blog
from blog.forms import BlogForm  # Explicit import
# from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import BlogPost  # Ensure you have BlogPost model imported
from .models import BlogPost

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/detail.html', {'post': post})

# def add_blog(request):
#     return render(request, 'blog/addblog.html')

def add_blog(request):
    print("✅ add_blog view reached!")  # Debugging print

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)  # ✅ Include request.FILES
        print("Form Data:", request.POST)  # Print form data
        print("File Data:", request.FILES)  # Print uploaded file details
        
        if form.is_valid():
            print("✅ Form is valid!")  # Debugging print
            blog = form.save(commit=False)
            blog.author = request.user  # Ensure user is logged in
            blog.save()
            print("✅ Blog saved successfully!")  # Debugging print
            return redirect('blog_list')  # Ensure 'blog_list' exists in urls.py
        else:
            print("❌ Form errors:", form.errors)  # Print form errors if invalid

    else:
        form = BlogForm()

    return render(request, 'blog/addblog.html', {'form': form})




def blog_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/blog_list.html", {"posts": posts})



def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, "blog/blog_details.html", {"post": post})

# def add_blog(request):
#     print("✅ add_blog view reached!")  # Debugging Print
#     return render(request, 'blog/addblog.html')



def test_view(request):
    return HttpResponse("Blog page is working!") 