from django.shortcuts import render,redirect

def index(request):
    return render(request, "index.html")


def redirect_to_blog(request):
    return redirect("blog_list")  # Redirect to the blog list view

