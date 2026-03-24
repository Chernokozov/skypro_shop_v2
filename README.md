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
- [ДЗ 27: Аутентификация в веб-приложениях](#Аутентификация в веб-приложениях)
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
категорий, управление товарами через админку и адаптивный интерфейс на Bootstrap 5 и полноценную аутентификацию
пльзователей.

**Основные цели проекта:**

- Освоение Django Framework
- Работа с базами данных
- Создание адаптивных интерфейсов
- Реализация CRUD-операций
- Работа с формами и валидацией
- Реализация системы аутентификации и регистрации пользователей

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
- **Регистрация и аутентификация пользователей**
- **Подтверждение email** при регистрации
- **Ограничение доступа** к CRUD операциям

### 🚧 В разработке

- Корзина покупок
- Система заказов
- Аутентификация пользователей
- Отзывы и рейтинги товаров
- Восстановление пароля

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

### ДЗ 27: Пользователи и аутентификация

**Ветка:** `feature/homework_27`

#### ✅ Реализованные требования:

#### 1. **Работа с Git и GitHub**

- [x] Домашка сдана через pull request из ветки домашней работы в ветку develop
- [x] В коммиты не добавлены игнорируемые файлы

#### 2. **Базовые настройки проекта**

- [x] В проекте есть файл с зависимостями (`requirements.txt`)

#### 3. **Работа с пользователями**

- [x] Создано новое приложение `users` для работы с пользователями
- [x] Реализована модель `User`, которая отнаследована от `AbstractUser`
- [x] В модель добавлены поля:
    - `email` (уникальный, обязательный)
    - `avatar` (изображение, необязательный)
    - `phone` (номер телефона, необязательный)
    - `country` (страна, необязательный)
- [x] Переопределено поле авторизации на `email`
- [x] Сделаны и запушены миграции нового приложения
- [x] В настройках проекта заменена `AUTH_USER_MODEL` на `users.User`
- [x] Произведены базовые настройки модели

#### 4. **Регистрация**

- [x] Создана форма `UserRegisterForm` для регистрации пользователя
- [x] Создан контроллер `UserCreateView` для регистрации
- [x] Определены и собраны шаблоны для регистрации (`register.html`)
- [x] Шаблоны рендерятся корректно
- [x] В интерфейс интегрирована кнопка регистрации
- [x] Переопределен метод `form_valid()` в контроллере регистрации
- [x] Интегрирована отправка письма с подтверждением email
- [x] Произведены настройки почтового сервера в `settings.py`

#### 5. **Авторизация**

- [x] Реализована авторизация пользователя через `LoginView`
- [x] Реализована форма авторизации
- [x] Реализован шаблон для логина (`login.html`)
- [x] Шаблон рендерится корректно
- [x] В интерфейс интегрирована кнопка входа
- [x] Реализован выход пользователя через `LogoutView`

#### 6. **Ограничение доступа**

- [x] Контроллеры для работы с продуктами дополнительно наследуются от `LoginRequiredMixin`
- [x] Общедоступной осталась только страница просмотра списка товаров

#### 7. **Подтверждение email**

- [x] Реализована верификация email через токен
- [x] После подтверждения пользователь активируется
- [x] Добавлен автоматический вход после подтверждения email
- [x] Перенаправление на главную страницу после верификации

### 🔧 Реализованные файлы:

#### **`users/models.py`**

```python
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='users/', null=True, blank=True)
    phone = models.CharField(max_length=35, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    token = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

```

#### **`users/forms.py`**

```python
class UserRegisterForm(ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)
    # ... валидация паролей и стилизация
```

#### **`users/views.py`**

```python
class UserCreateView(CreateView):
    """Регистрация пользователя с отправкой письма подтверждения"""
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')


def email_verification(request, token):
    """Подтверждение email и автоматический вход"""
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.token = ''
    user.save()
    login(request, user)
    return redirect('catalog:index')
```

#### **`config/settings.py`(обновлено)**

```python
AUTH_USER_MODEL = 'users.User'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'  # или ваш почтовый сервер
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = 'your-email@yandex.ru'
EMAIL_HOST_PASSWORD = 'your-password'
```

### 🧪 Тестирование функционала:

### Регистрация:

```text
URL: http://localhost:8000/users/register/
1. Заполнить форму регистрации
2. Нажать "Зарегистрироваться"
3. Получить письмо с подтверждением
4. Перейти по ссылке из письма
5. Автоматически войти в систему
```

### Авторизация:

```text
URL: http://localhost:8000/users/login/
1. Ввести email и пароль
2. Нажать "Войти"
3. Перенаправление на главную страницу
```

### Ограничение доступа:

```text
Страницы, требующие авторизации:
- /product/create/ - создание товара
- /product/update/<id>/ - редактирование товара
- /product/delete/<id>/ - удаление товара

 Доступны без авторизации:
- / - главная страница
- /catalog/ - каталог товаров
- /users/login/ - вход
- /users/register/ - регистрация
```

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

### 📊 Критерии выполнения ДЗ 27:

Критерий Статус Комментарий
Модель User от AbstractUser ✅ Добавлены кастомные поля
Авторизация по email ✅ USERNAME_FIELD = 'email'
Миграции выполнены ✅ Созданы и применены
Форма регистрации ✅ UserRegisterForm
Контроллер регистрации ✅ UserCreateView
Шаблоны регистрации ✅ register.html, login.html
Отправка email ✅ Подтверждение регистрации
Автоматический вход ✅ После подтверждения email
LoginRequiredMixin ✅ Для CRUD товаров
Кнопки в интерфейсе ✅ Вход, регистрация, выход
Git workflow ✅ Ветка feature/homework_27

### 🎯 Что нового было изучено:

1. Работа с Django Forms и ModelForm
2. Кастомная валидация через методы `clean_<fieldname>()`
3. Стилизация форм через переопределение `__init__`
4. Использование Class-Based Views для CRUD
5. Валидация файлов (изображений)
6. Обработка ошибок формы в шаблонах
7. Кастомизация модели пользователя через AbstractUser
8. Настройка аутентификации по email
9. Создание форм для регистрации с подтверждением пароля
10. Отправка email через SMTP
11. Генерация и использование токенов для верификации
12. Автоматический вход после подтверждения
13. Ограничение доступа с LoginRequiredMixin
14. Работа с Django Messages для уведомлений

### 🔗 Ссылки на код:

- Форма продукта: [`catalog/forms.py`](catalog/forms.py)
- CRUD контроллеры: [`catalog/views.py`](catalog/views.py)
- Шаблоны форм: [`catalog/templates/catalog/`](catalog/templates/catalog/)
- URL конфигурация: [`catalog/urls.py`](catalog/urls.py)
- Модель пользователя: [`users/models.py`](users/models.py)
- Форма регистрации: [`users/forms.py`](users/forms.py)
- Контроллеры: [`users/views.py`](users/views.py)
- URL конфигурация: [`users/urls.py`](users/urls.py)
- Шаблоны: [`users/templates/users/`](users/templates/users/)
- Настройки проекта: [`config/settings.py`](config/settings.py)

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
├── catalog/                 # Приложение каталога
│   ├── forms.py            # Формы товаров (ДЗ 26)
│   ├── models.py           # Модели Category, Product
│   ├── views.py            # Контроллеры CRUD
│   ├── urls.py             # URL приложения
│   ├── templates/          # Шаблоны каталога
│   └── fixtures/           # Тестовые данные
├── blog/                   # Приложение блога
│   ├── models.py           # Модель BlogPost
│   ├── views.py            # Контроллеры блога
│   └── templates/          # Шаблоны блога
├── users/                  # Приложение пользователей (ДЗ 27)
│   ├── forms.py            # Форма регистрации
│   ├── models.py           # Кастомная модель User
│   ├── views.py            # Регистрация, верификация
│   ├── urls.py             # URL пользователей
│   └── templates/          # Шаблоны авторизации
├── config/                 # Настройки проекта
│   ├── settings.py         # Основные настройки
│   ├── urls.py             # Главные URL
│   └── asgi.py, wsgi.py    # Конфигурация ASGI/WSGI
├── media/                  # Загруженные файлы
├── static/                 # Статические файлы
├── manage.py               # Утилита управления
├── requirements.txt        # Зависимости Python
├── .env                    # Переменные окружения
├── .gitignore             # Игнорируемые файлы
└── README.md              # Документация
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