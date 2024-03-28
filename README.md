# Работа с fast-api
## Установка и зависимости
1. Создание ВО: py -m venv venv
2. Установка fastapi и зависимостей: pip install fastapi[all]
## Первое приложение 
1. Создаём приложение:
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/") # Декоратор для точки входа по схеме Название-приложения.метод("путь")
def hello():
    return 'Hello world!'
```
2. Запускаем сервер командой: uvicorn main:app --reload | uvicorn <имя_файла:имя_приложения>
3. Просмотр документации: имя/docs или /redoc

## Привязываем БД
1. Качаем БД (PostgreSql)
2. Устанавливаем библиотеку для БД и миграций: pip install sqlalchemy alembic
3. Устанавливаем коннектер: pip install psycopg2 (для линукса добавляется -binary)
4. Создаём модели БД и применяем к ним миграции: alembic init migrations
5. В файле alembic.ini меняем DNS: sqlalchemy.url = driver://user:pass@localhost/dbname
6. Прописываем все перменные в файл env.py через секцию и устанавливаем метадату
7. Создаём ревизию: alembic revision --autogenerate (сравнивает текущее состояние БД с тем что есть на бэкенде) -m "Database creation"
8. Проводим миграцию: alembic upgrade <хэш_ревизии>, аналогично можно делать откат

## Регистрация и авторизация через библиотеку FastAPI Users
1. Устанавливаем библиотеку: pip install fastapi-users[sqlalchemy]
2. Устанавливаем асинхронный драйвер для работы с ДБ: pip install asyncpg
3. Создание модели пользователя







