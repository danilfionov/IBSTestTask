# Тестовый фреймворк для IBS TestTask

Этот тестовый фреймворк разработан для тестирования https://reqres.in/ - Открытое API

## Зависимости

Для запуска тестового фреймворка вам понадобятся следующие зависимости:

- Python 3.x
- pytest
- Selenium WebDriver
- requests

## Структура проекта

python
api
register
api.py
models.py
ui
pages
Main_Page.py
tests
api
configuration
conftest.py
test_CRUD
test_CRUD.py
ui
configuration
conftest.py
test_CRUD.py
schemas
resources.py
README.md

- `api/register/api.py`: Модуль, содержащий класс `CRUD` для взаимодействия с API CRUD операциями.
- `api/register/models.py`: Модуль, содержащий класс `CRUD_User` с методами для генерации данных для создания и обновления пользователя.
- `ui/pages/Main_Page.py`: Модуль, содержащий класс `Main_Page` для взаимодействия с пользовательским интерфейсом.
- `tests/api/configuration/conftest.py`: Модуль, содержащий фикстуру `url` для получения базового URL API.
- `tests/api/test_CRUD/test_CRUD.py`: Модуль, содержащий класс `TestCRUDApi` с тестами для операций CRUD на API.
- `tests/ui/configuration/conftest.py`: Модуль, содержащий фикстуру `driver` для инициализации WebDriver.
- `tests/ui/test_CRUD.py`: Модуль, содержащий класс `TestCRUD` с UI-тестами для взаимодействия с пользовательским интерфейсом.
- `schemas/resources.py`: Модуль, содержащий схемы данных для проверки ответов API.

## Запуск тестов

1. Установите зависимости, указанные в разделе "Зависимости".
2. Убедитесь, что API-сервер доступен и работает.
