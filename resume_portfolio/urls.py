from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from projects.views import project_list
from pages.views import page_detail
from skills.views import skill_list


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", page_detail, {"slug": "index"}, name="home"),
    path("projects/", project_list, name="project_list"),
    path("skills/", skill_list, name="skill_list"),
    path("<slug:slug>/", include("pages.urls")),
    path("tinymce/", include("tinymce.urls")),
    path("go/", include("shortlinks.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path(r"__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
