from django.contrib import admin
from .models import Project, Technology
from django.utils.html import format_html


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "display_technologies",
        "image_preview",
        "category_order",
        "created_at",
    )
    readonly_fields = ("image_preview",)
    list_filter = ("category", "technologies", "created_at")
    search_fields = ("title", "description")
    filter_horizontal = ("technologies",)  # виджет
    list_editable = (
        "category",
        "category_order",
    )

    def display_technologies(self, obj):
        return ", ".join([tech.name for tech in obj.technologies.all()])

    display_technologies.short_description = "технологии стека"

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 0px;" />',
                obj.image.url,
            )
        return "—"

    image_preview.short_description = "Превью"
