from django.urls import path
from .views import blog_list, blog_detail, add_blog

urlpatterns = [
    path("", blog_list, name="blog_list"),
    path("addblog/", add_blog, name="addblog"),  # ✅ Fix: Ensure add_blog is before dynamic patterns
    path("<int:post_id>/", blog_detail, name="blog_detail"),  # ✅ Keep int-based detail view
    path("<slug:slug>/", blog_detail, name="blog_detail"),  # ✅ Keep slug-based detail view
]
