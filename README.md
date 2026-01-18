# SkyproShop - Интернет-магазин на Django

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)
![Status](https://img.shields.io/badge/Status-Development-yellow)

Учебный проект интернет-магазина, разрабатываемый в рамках курса SkyPro.

## 📋 Оглавление

- [Обзор](#обзор)
- [Функциональность](#функциональность)
- [Домашнее задание 26: Формы](#домашнее-задание-26-формы)
- [Технологии](#технологии)
- [Установка](#установка)
- [Настройка](#настройка)
- [Разработка](#разработка)
- [Структура проекта](#структура-проекта)
- [Contributing](#contributing)
- [Лицензия](#лицензия)
- [Контакты](#контакты)

## 🎯 Обзор

SkyproShop - это полнофункциональный интернет-магазин, построенный на Django. Проект включает каталог товаров, систему
категорий, управление товарами через админку и адаптивный интерфейс на Bootstrap 5.

**Основные цели проекта:**

- Освоение Django Framework
- Работа с базами данных
- Создание адаптивных интерфейсов
- Реализация CRUD-операций
- Работа с формами и валидацией

## ✨ Функциональность

### ✅ Реализовано

- **Каталог товаров** с категориями и изображениями
- **Полный CRUD для товаров** через Django Forms
- **Валидация форм** с проверкой запрещенных слов
- **Блог статей** с полным CRUD
- **Административная панель** для управления контентом
- **Адаптивный дизайн** на Bootstrap 5
- **Загрузка изображений** для товаров и статей
- **Счетчик просмотров** для статей блога
- **Фильтрация** по статусу публикации

### 🚧 В разработке

- Корзина покупок
- Система заказов
- Аутентификация пользователей
- Отзывы и рейтинги товаров

## 🏆 Домашнее задание 26: Формы

### 📋 Задание выполнено в ветке: `feature/homework_26`

### ✅ Реализованные требования:

#### 1. **Формы для CRUD операций с продуктами**

- Создан класс `ProductForm` в `catalog/forms.py`
- Реализованы все CRUD-операции через Django Forms:
    - Создание продукта (`ProductCreateView`)
    - Чтение продукта (`ProductDetailView`)
    - Обновление продукта (`ProductUpdateView`)
    - Удаление продукта (`ProductDeleteView`)

#### 2. **Валидация запрещенных слов**

- Проверка названия и описания на запрещенные слова
- Запрещенные слова: `казино`, `криптовалюта`, `крипта`, `биржа`, `дешево`, `бесплатно`, `обман`, `полиция`, `радар`
- Валидация через методы `clean_name()` и `clean_description()`
- Регистронезависимая проверка

#### 3. **Кастомная валидация цены**

- Метод `clean_price()` проверяет, что цена не может быть отрицательной
- При ошибке выводится сообщение: "Цена не может быть отрицательной"

#### 4. **Стилизация форм**

- Все поля формы стилизованы через метод `__init__()`
- Использованы классы Bootstrap (`form-control`, `form-select`)
- Корректное отображение чекбокса для булевого поля `is_published`

#### 5. **Дополнительное задание (со звездочкой)**

- Валидация загружаемых изображений
- Проверка формата файла (JPEG, PNG)
- Проверка размера файла (не более 5 МБ)

### 🔧 Реализованные файлы:

#### **`catalog/forms.py`**

```python
class ProductForm(forms.ModelForm):
    FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', ...]

    def clean_name(self):

    # Проверка запрещенных слов в названии

    def clean_description(self):

    # Проверка запрещенных слов в описании

    def clean_price(self):

    # Проверка, что цена не отрицательная

    def clean_image(self):

    # Валидация изображения (формат, размер)

    def __init__(self, *args, **kwargs):
# Стилизация полей формы
```

#### **`catalog/views.py`** (добавлено)

```python
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
```

#### **`catalog/templates/catalog/`** (добавлено)

- `product_form.html` - форма создания/редактирования
- `product_confirm_delete.html` - подтверждение удаления

#### **`catalog/urls.py`** (обновлено)

```python
urlpatterns = [
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
]
```

### 🧪 Тестирование функционала:

#### 1. **Создание продукта:**

```
URL: http://localhost:8000/product/create/
Поля: название, описание, изображение, категория, цена, опубликовано
Валидация: запрещенные слова, отрицательная цена
```

#### 2. **Редактирование продукта:**

```
URL: http://localhost:8000/product/update/<id>/
Изменение: всех полей продукта
```

#### 3. **Удаление продукта:**

```
URL: http://localhost:8000/product/delete/<id>/
Подтверждение: через отдельную страницу
Перенаправление: на главную страницу после удаления
```

#### 4. **Тест валидации:**

```python
# Запрещенные слова
Название: "Лучшее казино в городе" → Ошибка: "Поле содержит запрещенное слово"
Описание: "Купите криптовалюту дешево" → Ошибка: "Поле содержит запрещенное слово"

# Отрицательная цена
Цена: -100 → Ошибка: "Цена не может быть отрицательной"

# Изображение
Формат:.txt → Ошибка: "Допустимые форматы изображений: JPEG, PNG"
Размер: 10
МБ → Ошибка: "Размер изображения не должен превышать 5 МБ"
```

### 📊 Критерии выполнения:

| Критерий                   | Статус | Комментарий                           |
|----------------------------|--------|---------------------------------------|
| Форма для продукта         | ✅      | `ProductForm` с полной валидацией     |
| CRUD операции              | ✅      | Create, Read, Update, Delete          |
| Валидация запрещенных слов | ✅      | В названии и описании                 |
| Валидация цены             | ✅      | Не может быть отрицательной           |
| Стилизация форм            | ✅      | Bootstrap классы через `__init__`     |
| Булевое поле как checkbox  | ✅      | `is_published` отображается корректно |
| URL маршруты               | ✅      | Все пути зарегистрированы             |
| Git workflow               | ✅      | Ветка `feature/homework_26`           |

### 🎯 Что нового было изучено:

1. Работа с Django Forms и ModelForm
2. Кастомная валидация через методы `clean_<fieldname>()`
3. Стилизация форм через переопределение `__init__`
4. Использование Class-Based Views для CRUD
5. Валидация файлов (изображений)
6. Обработка ошибок формы в шаблонах

### 🔗 Ссылки на код:

- Форма продукта: [`catalog/forms.py`](catalog/forms.py)
- CRUD контроллеры: [`catalog/views.py`](catalog/views.py)
- Шаблоны форм: [`catalog/templates/catalog/`](catalog/templates/catalog/)
- URL конфигурация: [`catalog/urls.py`](catalog/urls.py)

---

## 🛠️ Технологии

### Backend

- **Python 3.12** - основной язык программирования
- **Django 6.0** - веб-фреймворк
- **Pillow** - обработка изображений

### Frontend

- **Bootstrap 5** - CSS-фреймворк
- **JavaScript** - клиентские скрипты
- **HTML5/CSS3** - верстка

### База данных

- **PostgreSQL** - для разработки

## 🚀 Быстрый старт

```bash
# Клонирование и установка
git clone https://github.com/Chernokozov/skypro_shop.git
cd skypro_shop
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# или .venv\Scripts\activate  # Windows

# Установка зависимостей
pip install -r requirements.txt

# Настройка базы данных
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Загрузка тестовых данных
python manage.py loaddata catalog/fixtures/*.json

# Запуск сервера
python manage.py runserver
```

## 📁 Структура проекта

```
skypro_shop/
├── catalog/                 # Основное приложение
│   ├── forms.py           # Формы (домашка 26)
│   ├── models.py          # Модели данных
│   ├── views.py           # Контроллеры
│   ├── urls.py            # URL приложения
│   ├── templates/         # Шаблоны
│   │   └── catalog/
│   │       ├── product_form.html          # Форма товара
│   │       ├── product_confirm_delete.html # Удаление товара
│   │       ├── home.html                  # Главная страница
│   │       └── product_detail.html        # Детали товара
│   └── fixtures/          # Тестовые данные
├── blog/                  # Приложение блога
├── skypro_shop/           # Настройки проекта
├── manage.py             # Утилита управления
└── requirements.txt      # Зависимости Python
```

## 🤝 Contributing

1. Форкните репозиторий
2. Создайте ветку для новой функциональности
3. Внесите изменения и напишите тесты
4. Отправьте Pull Request

## 📄 Лицензия

MIT License - смотрите файл [LICENSE](LICENSE) для деталей.

## 👤 Автор

**Юрий Чернокозов**

- GitHub: [@Chernokozov](https://github.com/Chernokozov)
- Email: yorok352@mail.ru
- Telegram: @Yuriy_1843

## 🙏 Благодарности

- Команде SkyPro за отличный курс
- Сообществу Django за документацию и поддержку

---

**Примечание**: Это учебный проект, созданный для освоения Django и веб-разработки в рамках курса SkyPro.

```