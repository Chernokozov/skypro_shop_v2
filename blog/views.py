from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)

from .models import BlogPost


class BlogPostListView(ListView):
    """
    Отображение списка блоговых записей.
    Показывает только опубликованные записи.
    """

    model = BlogPost
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        """
        Фильтруем только опубликованные записи.
        Returns:
            QuerySet: Опубликованные записи.
        """
        return BlogPost.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        """
        Добавляем заголовок в контекст.
        Returns:
            dict: Контекст с заголовком.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Блог"
        return context


class BlogPostDetailView(DetailView):
    """
    Отображение детальной страницы записи.
    Увеличивает счётчики просмотров при открытии
    """

    model = BlogPost
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_object(self, queryset=None):
        """
        Подучаем объект и увеличиваем счётчик просмотров
        Args:
            queryset: Набор объектов для поиска.
        Returns:
            BlogPost: Найденная запись.
        """
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save(update_fields=["views_count"])
        return obj

    def get_context_data(self, **kwargs):
        """
        Добавляем заголовок в контекст.
        Returns:
            dict: Контекст с заголовком.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.title
        return context


class BlogPostCreateView(LoginRequiredMixin, CreateView):
    """
    Создание новой блоговой записи.
    Только для авторизованных пользователей.
    """

    model = BlogPost
    template_name = "blog/post_form.html"
    fields = ["title", "content", "preview", "is_published", "slug"]
    success_url = reverse_lazy("blog:post_list")

    def get_context_data(self, **kwargs):
        """
        Добавляем заголовок в контекст.
        Returns:
            dict: Контекст с заголовком.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Создание записи"
        return context


class BlogPostUpdateView(LoginRequiredMixin, UpdateView):
    """
    Редактирование существующей записи.
    Только для авторизованных пользователей.
    Перенаправляет на страницу записи после сохранения.
    """

    model = BlogPost
    template_name = "blog/post_form.html"
    fields = ["title", "content", "preview", "is_published", "slug"]
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_success_url(self):
        """
        Определяем куда перейти после сохранения.
        Returns:
            str: URL страницы записи.
        """
        return self.object.get_absolute_url()

    def get_context_data(self, **kwargs):
        """
        Добавляем заголовок в контекст.
        Returns:
            dict: Контекст с заголовком.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = f"Редактирование: {self.object.title}"
        return context


class BlogPostDeleteView(LoginRequiredMixin, DeleteView):
    """
    Удаление записи.
    Только для авторизованных пользователей.
    """

    model = BlogPost
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("blog:post_list")
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        """
        Добавляем заголовок в контекст.
        Returns:
            dict: Контекст с заголовком.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = f"Удаление: {self.object.title}"
        return context
