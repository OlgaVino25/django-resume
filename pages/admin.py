from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE

from .models import Page, PageImage


class PageImageInline(admin.TabularInline):
    model = PageImage
    extra = 1  # сколько пустых форм показывать
    fields = ("image", "caption", "order")
    ordering = ("order",)


class PageAdminForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={"cols": 80, "rows": 30}))

    class Meta:
        model = Page
        fields = "__all__"


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    form = PageAdminForm
    inlines = [PageImageInline]
    list_display = ("title", "slug", "is_published", "updated_at")
    list_filter = ("is_published",)
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}  # slug заполняется из title
