from django.contrib import admin
from .models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "level", "description", "category_order")
    list_filter = ("name", "category", "level")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    list_editable = (
        "level",
        "category_order",
    )
