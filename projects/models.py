from django.db import models


class Technology(models.Model):
    name = models.CharField("название", max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "технология стека"
        verbose_name_plural = "технологии стека"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify

            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Project(models.Model):

    class Category(models.TextChoices):
        PYTHON_BASICS = "python_basics", "Основы Python"
        GIT_GITHUB = "git_github", "Git и GitHub"
        API = "api", "API веб-сервисов"
        LAYOUT = "layout", "Вёрстка"
        DJANGO = "django", "Django-проекты"
        BOTS = "bots", "Чат-боты"
        TEAM = "team", "Командные проекты"
        OTHER = "other", "Другое"

    title = models.CharField("название", max_length=200)
    description = models.TextField("описание")
    technologies = models.ManyToManyField(
        Technology, verbose_name="технологии стека", blank=True, related_name="projects"
    )
    category = models.CharField(
        "категория",
        max_length=20,
        choices=Category.choices,
        default=Category.OTHER,
        db_index=True,
    )
    category_order = models.PositiveSmallIntegerField(
        "порядок категории", default=0, help_text="Чем меньше число, тем выше категория"
    )
    image = models.ImageField(
        "изображение", upload_to="projects/", blank=True, null=True
    )
    github_url = models.URLField("GitHub", blank=True)
    demo_url = models.URLField(
        "демо", blank=True, help_text="Ссылка на работающий сайт / демо"
    )
    created_at = models.DateTimeField("дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("дата обновления", auto_now=True)

    class Meta:
        verbose_name = "проект"
        verbose_name_plural = "проекты"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
