from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    """
    Модель для хранения блоговых записей.
    Attributes:
        title (str): Заголовок записи.
        content (str): Текст записи.
        preview (ImageField): Изображение для превью.
        created_at (datetime): Дата создания.
        is_published (bool): Опубликована ли запись.
        views_count (int): Количество просмотров.
        slug (str): Уникальный идентификатор для URL.
    """

    title = models.CharField(max_length=200, verbose_name="Заголовок")

    content = models.TextField(verbose_name="Содержимое")

    preview = models.ImageField(
        upload_to="blog/previews/", verbose_name="Превью", null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    views_count = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров"
    )

    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL")

    class Meta:
        """
        Метаданные модели
        Attributes:
            verbose_name: Человекочитаемое имя в единственном числе.
            verbose_name_plural: Человекочитаемое имя во множественном числе.
            ordering: Сортировка по умолчанию.
        """

        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"
        ordering = ["-created_at"]

    def __str__(self):
        """
        Строковое представление объекта.
        Returns:
            str: Заголовок записи.
        """
        return self.title

    def get_absolute_url(self):
        """
        Возвращает абсолютный URL для записи.
        Returns:
            str: URL страница записи.
        """
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
