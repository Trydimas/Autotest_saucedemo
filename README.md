# Selenium Pytest Project

Этот проект содержит автотесты для сайта [saucedemo.com](https://www.saucedemo.com/) с использованием Python, Selenium и Pytest. Проект позволяет проводить тесты аутентификации, авторизации, а также проверку возможности выхода пользователя.

## Подготовка к запуску

1. Клонируйте репозиторий проекта.
```commandline
git clone https://github.com/Trydimas/Autotest_saucedemo.git
```
2. Установка зависимостей

```commandline
pip install -r .\requirements.txt
```

## Запуск

В каталоге /tests/ в командной строке введите команду запуска
```commandline
pytest test_auth.py --browser=chrome --browser-version=latest
```


