from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import index
from django.shortcuts import redirect


admin.autodiscover()

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("students/", include("students.urls")),
    path("register/", include("register.urls")),
    path("", index, name="index"),
    path("", include("cms.urls")), 
    
    
]



# urlpatterns += i18n_patterns(path("admin/", admin.site.urls), path("", include("cms.urls")))
urlpatterns += i18n_patterns(path('blog/', include('blog.urls')),) 


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

    
