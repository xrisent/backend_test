﻿# backend_test
###                                                                   Тестовое задание

Это проект написанный на Django, который предоставляет REST API для управления постами, комментариями и лайками к постам

## Особенности
- CRUD операции для постов, комментариев и лайков с пагинацией.
- Фильтрация постов по дате создания, автору и количеству лайков.
- Аутентификация и авторизация пользователей с помощью JWT токенов и встроенной модели User.
- Документация API с использованием Swagger UI.

## Установка
- Клонируйте проект
- git clone https://github.com/xrisent/backend_test.git
- Установите зависимости
- pip install -r req.txt
- Примените миграции
- python manage.py migrate
- Запустите сервер
- python manage.py runserver

## Endpoints
- admin/ - панель администратора
- api/v1/post/ - json-список постов с возможностью их фильтрации
- api/v1/comment/ - json-список комментариев
- api/v1/like/ - json-список лайков
- api/v1/user/ - создание user(post-запрос только)
- api/v1/token/ - получение токена для определенного user
- api/v1/token/refresh/ - обновление токена
- api/v1/token/verify/ - проверка токена на валидность
- swagger/ - документация

