from django.shortcuts import render
from .models import Project


def project_list(request):
    projects = Project.objects.prefetch_related("technologies").order_by(
        "category_order",
        "created_at",
    )
    return render(request, "projects/project_list.html", {"projects": projects})
