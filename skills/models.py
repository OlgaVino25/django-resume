from django.db import models


class Skill(models.Model):
    class Category(models.TextChoices):
        LANGUAGES = "lang", "Языки программирования"
        FRAMEWORKS = "fw", "Фреймворки"
        DATABASES = "db", "Базы данных"
        TOOLS = "tools", "Инструменты"
        LIBRARIES = "libraries", "Библиотеки"
        DEVOPS = "devops", "DevOps и инфраструктура"
        BOT = "bot", "Боты и API"
        OTHER = "other", "Теория и Soft Skills"

    class Level(models.TextChoices):
        BEGINNER = "1", "Знакомство"
        INTERMEDIATE = "2", "Начальный"
        ADVANCED = "3", "Средний"
        EXPERT = "4", "Продуктивный"

    name = models.CharField("название", max_length=50, unique=True)
    category = models.CharField(
        "категория", max_length=20, choices=Category.choices, default=Category.OTHER
    )
    category_order = models.PositiveSmallIntegerField(
        "порядок категории", default=0, help_text="Чем меньше число, тем выше категория"
    )
    level = models.CharField(
        "уровень", max_length=1, choices=Level.choices, default=Level.INTERMEDIATE
    )
    description = models.TextField("Примечание", blank=True)
    slug = models.SlugField("URL-идентификатор", unique=True, blank=True)
    icon = models.ImageField("иконка", upload_to="skills/icons/", blank=True, null=True)

    class Meta:
        verbose_name = "навык"
        verbose_name_plural = "навыки"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify

            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
