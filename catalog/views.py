from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from .forms import ProductForm
from .models import Product


class ProductListView(ListView):
    """
    Класс для отображения списка товаров на главной странице.
    Наследуется от ListView - стандартного класса для списков
    """

    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        """
        Добавляем дополнительные данные в контекст.
        Returns:
            dict: Контекст с заголовком страницы.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Каталог товаров"
        return context


class ProductDetailView(DetailView):
    """
    Класс для отображения детальной страницы товара.
    Наследуется от DetailView - для отображения одного объекта.
    """

    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        """
        Добавляем заголовок в контекст.
        Returns:
            dict: Контекст с заголовком страницы
        """
        context = super().get_context_data(**kwargs)
        context["title"] = self.object.name
        return context


class ContactsView(TemplateView):
    """
    Класс для отображения страницы контактов.
    Наследуется от TemplateView - для статических страниц.
    """

    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        """
        Добавляем заголовок в контекст
        Returns:
            dict: Контекст с заголовком страницы.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты"
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создание нового продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание продукта'
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование существующего продукта"""

    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование: {self.object.name}'
        return context


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление продукта"""
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Удаление: {self.object.name}'
        return context
