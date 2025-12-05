
# Интернет-магазин SkyproShop

Проект интернет-магазина на Django, создаваемый в рамках учебного курса.

## Технологии
- Python 3.9+
- Django 4.2
- Bootstrap 5
- Poetry (управление зависимостями)

## Установка и запуск

1. Клонировать репозиторий:
```bash
git clone <url-репозитория>
cd ishop_project
```
Установить Poetry (если не установлен):

```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Установить зависимости:

```bash
poetry install
```
Активировать виртуальное окружение:

```bash
poetry shell
```
Применить миграции:

```bash
python manage.py migrate
```
Запустить сервер:

```bash
python manage.py runserver
```
Открыть в браузере:

http://localhost:8000/ - главная страница

http://localhost:8000/contacts/ - контакты

Структура проекта
catalog/ - основное приложение магазина

skypro_shop/ - настройки проекта

templates/ - HTML шаблоны

Автор
Юрий Чернокозов

text

## 11. Запуск и проверка

```bash
# Активируем окружение Poetry
poetry shell

# Применяем миграции
python manage.py migrate

# Запускаем сервер
python manage.py runserver
```