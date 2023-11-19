# Проект Atomic Habits Tracker
В проекте на основе Django REST framework реализована бэкенд-часть веб-приложения трекера привычек по книге Джеймса Клира «Атомные привычки». 

## Настройка Atomic Habits Tracker
1. Клонирование репозитория
```commandline
git clone https://github.com/dariabushueva/Atomic_Habits_Tracker.git
```
2. Создание телеграм-бота и получение API-ключа
- Для создания Telegram-бота найдите в чате самого главного бота:
```commandline
https://t.me/BotFather
```
- Начните с ним диалог и выберите команду создания нового бота:
```commandline
/newbot  # create a new bot
```
- Введите имя вашего бота, которое отображается пользователям.
- Введите юзернейм вашего бота - это уникальный идентификатор, по которому бота можно будет найти. Также важно, чтобы имя заканчивалось на _bot
- Если имя подходит под все правила, BotFather предоставит API-ключ (токен) и полезные ссылки для использования бота

3. Настройка переменных окружения
В корне проекта создать файл .env, в который записать свои данные:
```commandline
DJANGO_SECRET_KEY=
PSQL_DB_NAME=atomic_habits
PSQL_USER=
PSQL_PASSWORD=
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379
CELERY_TASK_TRACK_STARTED=1
TELEGRAM_BOT_API_KEY=
TELEGRAM_CHAT_ID=
```

4. Сборка Docker контейнера
```commandline
docker-compose build
```

## Запуск Atomic Habits Tracker
1. Запуск Docker контейнера
```commandline
docker-compose up
```

2. Откройте страницу в веб-браузере и перейдите по адресу, указанному в консоли (обычно http://127.0.0.1:8000/).

## Доступ к Swagger UI
Документация API предоставляется с использованием интерфейса Swagger.
Взаимодействие с API по следующему URL: http://127.0.0.1:8000/swagger/