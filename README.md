# Проект Atomic Habits Tracker
В проекте на основе Django REST framework реализована бэкенд-часть веб-приложения трекера привычек по книге Джеймса Клира «Атомные привычки». 

# Запуск Atomic Habits Tracker
## 1. Клонирование репозитория
```commandline
git clone https://github.com/dariabushueva/Atomic_Habits_Tracker.git
```
## 2. Установка зависимостей
Создать виртуальное окружение:
```commandline
python -m venv venv
```
Активировать виртуальное окружение:
```commandline
venv\Scripts\activate.bat  для Windows
source venv/bin/activate  для Linux и MacOS
```
Установить зависимости:
```commandline
pip install -r requirements.txt
```

## 3. Установка и запуск Redis
Установка:
```commandline
sudo apt-get install redis-server
```
Запуск:
```commandline
sudo service redis-server start
```

## 4. Установка и настройка PostgreSQL
Установка:
```commandline
sudo apt-get install postgresql
```
Запуск:
```commandline
psql -U postgres
```
Создание базы данных, где atomic_habits - название базы данных, которое можно изменить в файле .env
```commandline
CREATE DATABASE atomic_habits;
```
Закрыть PostgreSQL:
```commandline
\q
```

## 5. Создание телеграм-бота и получение API-ключа
Для создания Telegram-бота найдите в чате самого главного бота:
```commandline
https://t.me/BotFather
```
Начните с ним диалог и выберите команду создания нового бота:
```commandline
/newbot  # create a new bot
```
Введите имя вашего бота, которое отображается пользователям.

Введите юзернейм вашего бота - это уникальный идентификатор, по которому бота можно будет найти. Также важно, чтобы имя заканчивалось на _bot

Если имя подходит под все правила, BotFather предоставит API-ключ (токен) и полезные ссылки для использования бота

## 6. Настройка переменных окружения
В папке config/ создать файл .env, в который записать свои данные:
```commandline
DJANGO_SECRET_KEY=
PSQL_DB_NAME=atomic_habits
PSQL_USER=
PSQL_PASSWORD=
CELERY_BROKER_URL=
CELERY_RESULT_BACKEND=
CELERY_TASK_TRACK_STARTED=1
TELEGRAM_BOT_API_KEY=
TELEGRAM_CHAT_ID=
```

## 7. Применение миграций
```commandline
python manage.py migrate
```

## 8. Наполнение базы данных. Все данные предоставлены только в качестве примера.
```commandline
python manage.py loaddata habits_data.json
python manage.py loaddata users_data.json
```

## 9. Запуск сервера Django
```commandline
python manage.py runserver
```

## 10. Запуск сервиса периодических задач CELERY осуществляется в разных терминалах двумя командами
```commandline
python.exe -m celery -A config worker -l INFO -P eventlet 
celery -A config beat -l INFO -S django  
```