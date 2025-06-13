from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from cms.sitemaps import CMSSitemap
from django.conf.urls.i18n import i18n_patterns
from myproject.views import index, gallery, contact_view
admin.autodiscover()

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    path("admin/", admin.site.urls),
    path("news/", include("news.urls")),
    path("blog/", include("blog.urls")),
    path("students/", include("students.urls")),
    path("register/", include("register.urls")),
    path("faculty/", include("faculty.urls")),
    path("mission/", include("mission.urls")),
    path('publications/', include('publications.urls')),
    path('team/', include('team.urls')),
    path('contact/', contact_view, name='contact'),  # Add the missing comma here
    path("gallery/", gallery, name="gallery"),  # Ensure this line is correct


    path("", index, name="index"),
    path("", include("cms.urls")),
]

# i18n CMS URLs
urlpatterns += i18n_patterns(
    path("blog/", include("blog.urls")),
)

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
