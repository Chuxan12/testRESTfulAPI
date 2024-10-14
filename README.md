# User Management API

Этот проект представляет собой RESTful API для управления пользователями и их записями, разработанный с использованием FastAPI, SQLAlchemy, Redis и PostgreSQL.

## Оглавление

- [Требования](#требования)
- [Установка](#установка)
- [Запуск проекта](#запуск-проекта)
- [Использование](#использование)

## Требования

Перед началом убедитесь, что у вас установлены следующие компоненты:

- Python 3.8 или выше
- PostgreSQL
- Redis
- Docker и Docker Compose (опционально, для контейнеризации)

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/yourusername/user-management-api.git
   cd user-management-api

2. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt

4. Настройте файл .env для хранения конфигурационных параметров (например, строки подключения к базе данных):

Пример содержимого файла .env:
```bash
POSTGRES_USER=test
POSTGRES_PASSWORD=password
POSTGRES_DB='test'
POSTGRES_PORT=5432
POSTGRES_HOST=localhost
REDIS_URL=redis://redis:6379/0
REDIS_PORT=6379
FASTAPI_CACHE_LIFETIME=60
SECRET_KEY='your_secret_key'
ALGORITHM ='HS256'
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. (Опционально) Если вы хотите использовать Docker, выполните команду:

docker-compose up -d
## Запуск проекта
Для запуска проекта выполните:
   ```bash
   uvicorn app.api.main:app --host 0.0.0.0 --port 8000 --reload
   ```
   Теперь API будет доступен по адресу http://127.0.0.1:8000.

## Использование
API предоставляет следующие эндпоинты:

POST /auth/register: Регистрация нового пользователя<br />
POST /auth/login: Авторизация пользователя<br />
POST /auth/logout: Разлогинивание пользователя<br />
POST /tasks: Создание новой записи<br />
GET /tasks: Получение списка всех записей текущего пользователя<br />
GET /tasks/{task_id}: Получение конкретной записи<br />
Для более подробной информации о каждом эндпоинте вы можете обратиться к автоматически сгенерированной документации FastAPI по адресу http://127.0.0.1:8000/docs.