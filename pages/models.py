from django.db import models
from django.utils.text import slugify


class Page(models.Model):
    title = models.CharField("заголовок", max_length=200)
    slug = models.SlugField(
        "URL-идентификатор",
        unique=True,
        help_text="Уникальная строка для адреса страницы, например 'about'",
    )
    content = models.TextField("содержимое", blank=True)
    is_published = models.BooleanField("опубликовано", default=True)
    created_at = models.DateTimeField("дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("дата обновления", auto_now=True)

    class Meta:
        verbose_name = "страница"
        verbose_name_plural = "страницы"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # автоматическое заполнение slug из title, если не указано
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class PageImage(models.Model):
    page = models.ForeignKey(
        Page, on_delete=models.CASCADE, related_name="images", verbose_name="страница"
    )
    image = models.ImageField(
        "изображение", upload_to="pages/", blank=False, null=False
    )
    caption = models.CharField(
        "подпись",
        max_length=200,
        blank=True,
        help_text="Необязательная подпись под фото",
    )
    order = models.PositiveSmallIntegerField(
        "порядок", default=0, help_text="Чем меньше число, тем выше в списке"
    )

    class Meta:
        verbose_name = "изображение страницы"
        verbose_name_plural = "изображения страницы"
        ordering = ["order"]

    def __str__(self):
        return f"Изображение для {self.page.title} (№{self.order})"
